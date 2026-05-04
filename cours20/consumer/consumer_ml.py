import os
import json
from confluent_kafka import Consumer, Producer

# KAFKA_BROKER = "kafka:9092"
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

consumer = Consumer({
    "bootstrap.servers": KAFKA_BROKER,
    'group.id': 'ml-group',
    'auto.offset.reset': 'earliest',
    'fetch.min.bytes': 1 
})

consumer.subscribe(['telemetry'])

producer = Producer({
    'bootstrap.servers': KAFKA_BROKER,
    'linger.ms': 0
})

print(f"IA en attente de données sur {KAFKA_BROKER}...")

try:
    while True:
        msg = consumer.poll(0.1)

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
        
        producer.flush(0) 

        print(f"Diagnostic : {status}")

except KeyboardInterrupt:
    print("Arrêt de l'IA...")
finally:
    consumer.close()