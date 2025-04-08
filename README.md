🚦 Adaptive Load Balancer - A Smart Traffic Director for Web Services 🚀
No stress, just success! 🧠💻🌐
Welcome to our software-defined adventure into the world of intelligent traffic handling! This project is a containerized, scalable, and self-contained load balancer deployed in an Azure VM that intelligently distributes HTTP requests based on real-time server stress 🧘‍♂️⚖️.

🧠 Project Overview
This project creates a simple, yet effective, Weighted Round Robin Load Balancer using Python Flask and Docker. The goal is to distribute incoming traffic efficiently and adaptively without external tools like Nginx or HAProxy.

📦 All containers. No clutter.
🔥 All Python. No panic.

🛠️ Tech Stack & Features
🐳 Docker + Docker Compose

🌐 Azure VM Deployment

🧪 Flask-based Web Services

⚖️ Weighted Random Selection Algorithm

📊 Dynamic load-aware traffic distribution

🔧 Live system stress metric fetching

📈 Scalable and maintainable microservice design

⚙️ Architecture in Action
The system includes:

Three Flask-based Web Servers 🧱🧱🧱

One Python-based Load Balancer 🔁

All linked in a Docker Compose network 🕸️

Each incoming request is:

📥 Received by the load balancer.

📊 Stress values (CPU, RAM) are fetched.

⚖️ Adjusted weights are computed.

🎯 A backend server is chosen smartly.

🔁 Response is forwarded back to the client.

📦 How to Run
bash
Copy
Edit
# Clone the repo
git clone https://github.com/your-username/adaptive-load-balancer.git
cd adaptive-load-balancer

# Build and run containers
docker-compose up --build
Then open your browser and visit:
📍 http://<your-azure-vm-ip>
To view stress:
📍 http://<your-azure-vm-ip>/metrics

📉 Example: Dynamic Load Distribution
Low Stress Scenario

Server	Original Weight	Adjusted Weight
Server1	3	2.4
Server2	2	1.6
Server3	2	1.6
High Stress Scenario

Server	Original Weight	Adjusted Weight
Server1	3	1.71
Server2	2	1.14
Server3	2	1.14
✅ Status
 Dockerized Flask microservices

 Load Balancer with Weighted Random Selection

 Real-time stress monitoring and adaptive traffic routing

 Fully working on Azure VM

💡 Conclusion
This Adaptive Load Balancer is perfect for:

Learning about SDN and cloud-native architectures

Building scalable microservice systems

Enhancing fault tolerance and performance

“Balance is not something you find, it’s something you create… with Python and Docker.” 🧘‍♀️🐍🐳

👨‍💻 Authors
Prudhvi Ponnada

Sai Siri Sree Venturi

Want to contribute or have suggestions?
📬 Open an issue or fork the repo!
