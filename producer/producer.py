from kafka import KafkaProducer
import time
import random
import uuid

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def generate_random_text():
    texts = [
        "Harika bir deneyimdi, kesinlikle tekrar geleceğim!",
        "Servis biraz yavaştı, ama yemekler lezzetliydi.",
        "Ortam çok şık ve rahat, tavsiye ederim.",
        "Fiyatlar biraz yüksek, ancak kalite iyi.",
        "Nötr bir deneyimdi, ne iyi ne de kötü."
    ]
    return random.choice(texts)

while True:
    comment_id = str(uuid.uuid4())
    text = generate_random_text()
    message = f"{comment_id},{text}"
    producer.send('raw-comments', value=message.encode('utf-8'))
    print(f"Sent: {message}")
    time.sleep(random.choice([0.1, 10]))