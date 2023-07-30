from kafka import KafkaConsumer
from SendEmailCustomerio import sendEmail 
import time
import json

bootstrap_server = 'localhost:9092'
topic = 'onboarding_email'
consumer = KafkaConsumer(topic, bootstrap_server)

for message in consumer:
    parsedMessage = json.loads(message.value.decode('utf-8'))

    sendEmail(parsedMessage["message_id"], parsedMessage["message_subject"], parsedMessage["message_body"])
    time.sleep(1)