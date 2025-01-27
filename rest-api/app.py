from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname=comments user=postgres password=postgres")

@app.route('/comments', methods=['GET'])
def get_comments():
    sentiment_filter = request.args.get('category')
    query = "SELECT comment_id, text, sentiment FROM comments"
    if sentiment_filter:
        query += f" WHERE sentiment = '{sentiment_filter}'"
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    comments = [{"comment_id": row[0], "text": row[1], "sentiment": row[2]} for row in results]
    return jsonify(comments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)