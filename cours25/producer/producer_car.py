import os
import time
import json
import random
from confluent_kafka import Producer

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

# --- MODIFICATION SPÉCIFIQUE SWARM : ATTENTE ACTIVE ---
def get_producer(broker):
    while True:
        try:
            p = Producer({
                'bootstrap.servers': broker,
                'client.id': 'car-sensor-swarm',
                'acks': 1
            })
            # On teste la connexion en demandant les métadonnées
            p.list_topics(timeout=5)
            print("Connecté à Kafka sur le cluster Swarm !")
            return p
        except Exception as e:
            print(f"En attente de Kafka ({broker})... Réessai dans 5s")
            time.sleep(5)

p = get_producer(KAFKA_BROKER)

try:
    while True:
        data = {"vibration": round(random.uniform(0.5, 5.0), 2), "temp": random.randint(70, 120)}
        
        # On utilise une gestion d'erreur sur le produce aussi
        try:
            p.produce('telemetry', json.dumps(data).encode('utf-8'))
            p.flush(0)
            print(f"Envoyé : {data}")
        except BufferError:
            print("Buffer plein, attente...")
            p.poll(1)
            
        time.sleep(1)
except KeyboardInterrupt:
    print("Arrêt...")