import os
import json
import time
import threading
from flask import Flask, jsonify
from confluent_kafka import Consumer

app = Flask(__name__)

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
TOPIC = "alerts"

latest_alert = {"status": "En attente..."}


# Attente Kafka
def wait_for_kafka():
    while True:
        try:
            c = Consumer({
                'bootstrap.servers': KAFKA_BROKER,
                'group.id': 'health-check'
            })
            c.list_topics(timeout=5)
            c.close()
            print("Kafka prêt !")
            return
        except Exception:
            print("Kafka indisponible... retry")
            time.sleep(3)


# Attente topic
def wait_for_topic():
    while True:
        try:
            c = Consumer({
                'bootstrap.servers': KAFKA_BROKER,
                'group.id': 'topic-check'
            })
            topics = c.list_topics(timeout=5).topics
            c.close()

            if TOPIC in topics:
                print(f"Topic {TOPIC} prêt !")
                return
            else:
                print(f"Topic {TOPIC} absent...")
        except Exception:
            print("Erreur check topic")

        time.sleep(3)


def create_consumer():
    return Consumer({
        'bootstrap.servers': KAFKA_BROKER,
        'group.id': 'api-group',
        'auto.offset.reset': 'latest',
        'broker.address.family': 'v4'
    })


#   Thread Kafka robuste
def consume():
    global latest_alert

    wait_for_kafka()
    wait_for_topic()

    consumer = create_consumer()
    consumer.subscribe([TOPIC])

    print("API connectée à Kafka")

    while True:
        try:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                print(f"Erreur Kafka: {msg.error()}")
                continue

            latest_alert = json.loads(msg.value().decode('utf-8'))

        except Exception as e:
            print(f"Erreur consumer: {e}")
            time.sleep(3)

            #  recrée le consumer si problème
            try:
                consumer.close()
            except:
                pass

            consumer = create_consumer()
            consumer.subscribe([TOPIC])


# lancement thread
threading.Thread(target=consume, daemon=True).start()


@app.route('/status')
def get_status():
    return jsonify(latest_alert)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)