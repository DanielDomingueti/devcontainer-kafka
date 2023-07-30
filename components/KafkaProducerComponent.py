import json
import time
from kafka import KafkaProducer

bootstrap_server = 'localhost:9092'
topic = 'onboarding_email'
kafkaProducer = KafkaProducer(bootstrap_servers=bootstrap_server)

message_limit = 5
topic = 'onboarding_email'

for i in range(message_limit):
    message = {
        "message_id": i,
        "message_user_email": "client{i}@email.com",
        "message_body": "Onboarding message"
    }
    kafkaProducer.send(topic, json.dumps(message).encode("UTF-8"))
    print(f"Sent email: {i}")
    time.sleep(1)

