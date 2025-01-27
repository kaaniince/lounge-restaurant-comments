import grpc
from concurrent import futures
import random
import time
import sentiment_analyzer_pb2
import sentiment_analyzer_pb2_grpc

class SentimentAnalyzerServicer(sentiment_analyzer_pb2_grpc.SentimentAnalyzerServicer):
    def AnalyzeSentiment(self, request, context):
        text = request.text
        sentiment = self._get_sentiment(text)
        time.sleep(len(text) * 0.01) 
        return sentiment_analyzer_pb2.SentimentResponse(sentiment=sentiment)

    def _get_sentiment(self, text):
        sentiments = ["positive", "negative", "neutral"]
        return random.choice(sentiments)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sentiment_analyzer_pb2_grpc.add_SentimentAnalyzerServicer_to_server(SentimentAnalyzerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()