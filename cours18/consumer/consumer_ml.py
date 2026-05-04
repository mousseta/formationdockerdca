import os
import json
from confluent_kafka import Consumer, Producer
KAFKA_BROKER = "kafka:9092"
consumer = Consumer({
     "bootstrap.servers": KAFKA_BROKER,
    'group.id': 'ml-group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['telemetry'])

producer = Producer({'bootstrap.servers': KAFKA_BROKER})

print("IA en attente de données...")

while True:

    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print("Erreur Kafka:", msg.error())
        continue

    if msg.value() is None:
        continue

    try:
        data = json.loads(msg.value().decode('utf-8'))
    except json.JSONDecodeError:
        print("Message invalide :", msg.value())
        continue

    status = "DANGER" if data['temperature'] > 105 or data['vibration'] > 4.5 else "OK"

    alert = {
        "status": status,
        "vibration": data['vibration'],
        "temperature": data['temperature']
    }

    producer.produce('alerts', json.dumps(alert).encode('utf-8'))
    producer.poll(0)

    print(f"Diagnostic : {status}")