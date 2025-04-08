# 🚦 Adaptive Load Balancer - A Smart Traffic Director for Web Services 🚀

*No stress, just success!* 🧠💻🌐

Welcome to our software-defined adventure into the world of intelligent traffic handling!  
This project is a **containerized, scalable, and self-contained load balancer** deployed in an Azure VM that intelligently distributes HTTP requests based on real-time server stress 🧘‍♂️⚖️.

---

## 🧠 Project Overview

This project creates a simple, yet effective, **Weighted Round Robin Load Balancer** using Python Flask and Docker.  
The goal is to distribute incoming traffic **efficiently and adaptively** without external tools like Nginx or HAProxy.

- 📦 **All containers. No clutter.**
- 🔥 **All Python. No panic.**

---

## 🛠️ Tech Stack & Features

- 🐳 Docker + Docker Compose  
- 🌐 Azure VM Deployment  
- 🧪 Flask-based Web Services  
- ⚖️ Weighted Random Selection Algorithm  
- 📊 Dynamic load-aware traffic distribution  
- 🔧 Live system stress metric fetching  
- 📈 Scalable and maintainable microservice design  

---

## ⚙️ Architecture in Action

**Components:**

- 🧱 Three Flask-based Web Servers  
- 🔁 One Python-based Load Balancer  
- 🕸️ All linked in a Docker Compose network

**Request Flow:**

1. 📥 Request hits the load balancer.
2. 📊 Stress values (CPU, RAM) fetched.
3. ⚖️ Weights are adjusted.
4. 🎯 Smart backend selection.
5. 🔁 Response routed to client.

---
# Authors

*Lab rats caught* 🧠💻🌐

*Don't get angry, eat jangiri*😅😹

Prudhvi Ponnada: ponnadaprudhvi18@gmail.com
Siri Venturi: really rat, s3.venturi@gmail.com 🧘‍♂️.

---
## 📦 How to Run

```bash
# Clone the repo
git clone https://github.com/prudhviponnada/Dynamic_loadbalancer
cd Dynamic_loadbalancer

# Build and run containers
docker-compose up --build
