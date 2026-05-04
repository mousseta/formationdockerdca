import os
import time
import json
from confluent_kafka import Consumer

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

def create_consumer():
    while True:
        try:
            print(f"Tentative de connexion à {KAFKA_BROKER}...")
            c = Consumer({
                'bootstrap.servers': KAFKA_BROKER,
                'group.id': f'k8s-group-{time.time()}', # ID unique pour forcer la lecture fraîche
                'auto.offset.reset': 'earliest',
                'broker.address.family': 'v4'
            })
            c.subscribe(['telemetry'])
            c.list_topics(timeout=5)
            return c
        except Exception as e:
            print(f"Kafka indisponible. Nouvel essai dans 5s... {e}")
            time.sleep(5)

consumer = create_consumer()
print("IA FleetPulse connectée et prête sur Kubernetes.")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None: 
            continue
        if msg.error():
            print(f"Erreur flux: {msg.error()}")
            continue

        # Sécurisation de la lecture JSON
        try:
            data = json.loads(msg.value().decode('utf-8'))
            # Utilise .get() pour éviter le crash si la clé change entre 'temp' et 'temperature'
            temp = data.get('temperature') or data.get('temp')
            print(f" Analyse en temps réel : {temp}°C | Vibration: {data.get('vibration')}")
        except Exception as e:
            print(f"Erreur décodage JSON: {e}")

except KeyboardInterrupt:
    consumer.close()