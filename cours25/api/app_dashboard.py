from flask import Flask, jsonify
from confluent_kafka import Consumer
import json
import threading
import socket          # <-- ajout

app = Flask(__name__)
KAFKA_BROKER = "kafka:9092"
consumer = Consumer({
    'bootstrap.servers': KAFKA_BROKER,
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

@app.route('/whoami')
def whoami():
    return jsonify({
        "container": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname())
    })

@app.route('/status')
def get_status():
    response = jsonify(latest_alert)
    response.headers["X-Served-By"] = socket.gethostname()  
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)