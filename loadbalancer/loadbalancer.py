from flask import Flask, jsonify, request
import requests
import random
import psutil

app = Flask(__name__)

#  stress-ful url
METRICS_URL = "http://20.93.20.209:5000/metrics"

# weights lifting for the servers
servers = [
    {"url": "http://server1:5000", "weight": 3},
    {"url": "http://server2:5000", "weight": 2},
    {"url": "http://server3:5000", "weight": 2}
]

# Fetch stress from stress-ful url
def get_stress():
    try:
        response = requests.get(METRICS_URL, timeout=1)
        if response.status_code == 200:
            data = response.json()
            return data.get("stress", 1)  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching stress value: {e}")
    return 1  #  hoping it won't fail

# dynamically assigned weights due to stress eating by servers
def adjust_weights():
    stress = get_stress()
    for server in servers:
        server["adjusted_weight"] = max(0.1, server["weight"] / (1 + stress))  #  putting weight according to bmi

# Select a server based on adjusted weights
def select_server():
    adjust_weights()  # Ensure weights are updated before choosing a server
    weighted_servers = [server["url"] for server in servers]
    weights = [server["adjusted_weight"] for server in servers]
    return random.choices(weighted_servers, weights=weights, k=1)[0]

# Load balancing routes to its way
@app.route("/", methods=["GET"])
def load_balance():
    selected_server = select_server()
    print(f"Forwarding request to: {selected_server}")

    try:
        response = requests.get(selected_server)
        return response.text, response.status_code, response.headers.items()
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to reach {selected_server}. {str(e)}", 502

# know the stress
@app.route("/metrics", methods=["GET"])
def metrics():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    stress = (cpu_usage + memory_usage) / 200  # let's NORMALIZE the STRESS to range [0,1]

    return jsonify({
        "cpu": cpu_usage,
        "memory": memory_usage,
        "stress": stress
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080) #available to ipv4 devices from docker containers
