import json
import time
from confluent_kafka import Producer

bootstrap_servers = 'localhost:29092'
topic = 'onboarding_email'

producer = Producer({'bootstrap.servers': bootstrap_servers})

for i in range(5):  # Você pode ajustar o limite aqui, se desejar
    message = {
        "message_id": i,
        "message_subject": f"Onboarding subject {i}",
        "message_body": f"Onboarding message {i}"
    }
    producer.produce(topic, json.dumps(message).encode("UTF-8"))
    producer.flush()
    print(f"Sent email: {i}")
    time.sleep(1)

producer.flush()
