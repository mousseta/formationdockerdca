from flask import Flask, jsonify
from confluent_kafka import Consumer
import json
import threading

app = Flask(__name__)

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'api-group',
    'auto.offset.reset': 'latest'
})

consumer.subscribe(['alerts'])

latest_alert = {"status": "En attente..."}

def consume():
    global latest_alert

    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            continue

        latest_alert = json.loads(msg.value().decode('utf-8'))

threading.Thread(target=consume, daemon=True).start()

@app.route('/status')
def get_status():
    return jsonify(latest_alert)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)