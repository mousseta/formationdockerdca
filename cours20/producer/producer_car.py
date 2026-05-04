import os
import time
import json
import random
from confluent_kafka import Producer

# KAFKA_BROKER = "kafka:9092"
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

# p = Producer({
#     'bootstrap.servers': 'localhost:9092'
# })
p = Producer({
    "bootstrap.servers": KAFKA_BROKER,
    "linger.ms": 0,  
    "acks": 1       
})

def delivery_report(err, msg):
    if err is not None:
        print(f"Erreur : {err}")
    else:
        pass 

print(f"Simulateur Auto lancé sur {KAFKA_BROKER}...")

try:
    while True:
        data = {
            "vibration": round(random.uniform(0.5, 5.0), 2),
            "temperature": random.randint(70, 120),
            "speed": random.randint(50, 130)
        }

        p.produce(
            'telemetry',
            json.dumps(data).encode('utf-8'),
            callback=delivery_report
        )

        p.flush(0) 

        print(f"Envoi : {data}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Arrêt du producer...")
finally:
    p.flush(10)