from kafka import KafkaConsumer

bootstrap_servers = 'localhost:9091' #kafka1 instance
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
