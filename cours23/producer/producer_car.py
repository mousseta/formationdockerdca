import os
import time
import json
import random
from confluent_kafka import Producer

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

def wait_for_kafka(broker, retries=20, delay=5):
    from confluent_kafka.admin import AdminClient
    print(f"Attente de Kafka sur {broker}...")
    for i in range(retries):
        try:
            client = AdminClient({"bootstrap.servers": broker})
            client.list_topics(timeout=5)
            print("Kafka est prêt !")
            return
        except Exception as e:
            print(f"Tentative {i+1}/{retries} échouée : {e}")
            time.sleep(delay)
    raise RuntimeError("Kafka non disponible après plusieurs tentatives")

wait_for_kafka(KAFKA_BROKER)

p = Producer({
    "bootstrap.servers": KAFKA_BROKER,
    "linger.ms": 0,
    "acks": 1
})

def delivery_report(err, msg):
    if err is not None:
        print(f"Erreur : {err}")

print(f"Simulateur Auto lancé sur {KAFKA_BROKER}...")

try:
    while True:
        data = {
            "vibration": round(random.uniform(0.5, 5.0), 2),
            "temperature": random.randint(70, 120),
            "speed": random.randint(50, 130)
        }
        p.produce('telemetry', json.dumps(data).encode('utf-8'), callback=delivery_report)
        p.flush(0)
        print(f"Envoi : {data}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Arrêt du producer...")
finally:
    p.flush(10)