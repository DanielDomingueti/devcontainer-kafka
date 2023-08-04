from kafka import KafkaProducer
import time

bootstrap_servers = 'kafka:9092' 
topic_name = 'onboarding'

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    api_version=(3, 5, 1)
)

def send_message(producer, topic, message):
    producer.send(topic, value=message.encode('utf-8'))
    producer.flush()

messages = [
    "Mensagem 1",
    "Mensagem 2",
    "Mensagem 3"
]

for message in messages:
    print(f"Sent: {message}")
    send_message(producer, topic_name, message)
    time.sleep(1)

producer.close()
