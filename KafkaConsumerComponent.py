from kafka import KafkaConsumer

bootstrap_servers = '192.168.65.0:9092'
topic_name = 'onboarding'

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=bootstrap_servers,
    api_version=(3, 5, 1),
    group_id='onboarding-group'
)

def process_message(message):
    print(f"Received: {message.value.decode('utf-8')}")

try:
    for message in consumer:
        process_message(message)
except KeyboardInterrupt:
    pass
finally:
    consumer.close()