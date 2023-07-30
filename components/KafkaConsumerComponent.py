from kafka import KafkaConsumer
import SendEmailCustomerio as sendEmail
import time

bootstrap_server = 'localhost:9092'
topic = 'onboarding_email'
consumer = KafkaConsumer(topics=topic, bootstrap_servers = bootstrap_server)

for message in consumer:
    //pergar os valores da mensagem aqui
    sendEmail.execute(message, transactionalMessageId, subject, body)
    time.sleep(1)