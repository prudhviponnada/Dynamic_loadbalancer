import socket
from flask import Flask, jsonify
import os
import psutil

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hi from: {socket.gethostname()} please Verify me with docker-compose ps output!"

@app.route("/metrics")
def metrics():
    stress = psutil.cpu_percent() + psutil.virtual_memory().percent  
    return jsonify({
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "stress": stress/200
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
