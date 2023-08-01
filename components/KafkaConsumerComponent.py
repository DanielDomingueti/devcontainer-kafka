from confluent_kafka import Consumer, KafkaError
import time
import json

bootstrap_servers = 'localhost:29092'
topic = 'onboarding_email'
group_id = '17'  # Defina um group_id aqui

consumer = Consumer({
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': 'earliest'
})

consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("Fim da Partição")
            else:
                print(f"Erro ao receber mensagem: {msg.error()}")
        else:
            parsedMessage = json.loads(msg.value().decode('utf-8'))
            print(f"Mensagem recebida: {parsedMessage}")
            # Faça o que desejar com a mensagem recebida aqui

except KeyboardInterrupt:
    pass

finally:
    consumer.close()
