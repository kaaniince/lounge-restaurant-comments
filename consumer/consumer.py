from kafka import KafkaConsumer
import grpc
import sentiment_analyzer_pb2
import sentiment_analyzer_pb2_grpc
import psycopg2

consumer = KafkaConsumer('raw-comments', bootstrap_servers='localhost:9092')

channel = grpc.insecure_channel('localhost:50051')
stub = sentiment_analyzer_pb2_grpc.SentimentAnalyzerStub(channel)

conn = psycopg2.connect("dbname=comments user=postgres password=postgres")
cursor = conn.cursor()

for message in consumer:
    comment_id, text = message.value.decode('utf-8').split(',', 1)
    try:
        response = stub.AnalyzeSentiment(sentiment_analyzer_pb2.SentimentRequest(text=text))
        sentiment = response.sentiment
        cursor.execute("INSERT INTO comments (comment_id, text, sentiment) VALUES (%s, %s, %s)",
                       (comment_id, text, sentiment))
        conn.commit()
        print(f"Processed: {comment_id}, {text}, {sentiment}")
    except grpc.RpcError as e:
        print(f"Error processing comment {comment_id}: {e}")