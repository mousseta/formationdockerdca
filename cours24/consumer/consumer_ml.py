import os
import time
import json
from confluent_kafka import Consumer

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

def create_consumer():
    while True:
        try:
            c = Consumer({
                'bootstrap.servers': KAFKA_BROKER,
                'group.id': 'ml-swarm-group',
                'auto.offset.reset': 'earliest',
                'broker.address.family': 'v4' # Force l'IPv4 pour le réseau Overlay
            })
            c.subscribe(['telemetry'])
            # Test de présence du broker
            c.list_topics(timeout=5)
            return c
        except Exception as e:
            print(f"Kafka indisponible sur Swarm. Nouvel essai...")
            time.sleep(5)

consumer = create_consumer()

print("IA prête sur le cluster.")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None: continue
        if msg.error():
            print(f"Erreur flux: {msg.error()}")
            # Si l'erreur est grave, on recrée le consumer
            if msg.error().fatal():
                consumer = create_consumer()
            continue

        data = json.loads(msg.value().decode('utf-8'))
        print(f"Analyse : {data['temp']}°C")

except KeyboardInterrupt:
    consumer.close()