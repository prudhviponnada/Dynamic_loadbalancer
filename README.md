<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Adaptive Load Balancer</title>
  <style>
    body {
      font-family: "Segoe UI", sans-serif;
      line-height: 1.6;
      max-width: 900px;
      margin: auto;
      padding: 2em;
      background-color: #f9f9f9;
      color: #333;
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    code {
      background-color: #eee;
      padding: 2px 6px;
      border-radius: 4px;
    }
    pre {
      background-color: #272822;
      color: #f8f8f2;
      padding: 1em;
      border-radius: 6px;
      overflow-x: auto;
    }
    table {
      border-collapse: collapse;
      width: 100%;
      margin-top: 1em;
    }
    table, th, td {
      border: 1px solid #bbb;
      padding: 0.5em;
      text-align: center;
    }
    .emoji {
      font-size: 1.2em;
    }
  </style>
</head>
<body>

  <h1>🚦 Adaptive Load Balancer - A Smart Traffic Director for Web Services 🚀</h1>
  <h3><em>No stress, just success! 🧠💻🌐</em></h3>

  <p>Welcome to our software-defined adventure into the world of intelligent traffic handling! This project is a <strong>containerized, scalable, and self-contained load balancer</strong> deployed in an Azure VM that intelligently distributes HTTP requests based on real-time server stress 🧘‍♂️⚖️.</p>

  <h2>🧠 Project Overview</h2>
  <p>This project creates a simple, yet effective, <strong>Weighted Round Robin Load Balancer</strong> using Python Flask and Docker. The goal is to distribute incoming traffic <strong>efficiently and adaptively</strong> without external tools like Nginx or HAProxy.</p>
  <ul>
    <li>📦 <strong>All containers. No clutter.</strong></li>
    <li>🔥 <strong>All Python. No panic.</strong></li>
  </ul>

  <h2>🛠️ Tech Stack & Features</h2>
  <ul>
    <li>🐳 <strong>Docker</strong> + <strong>Docker Compose</strong></li>
    <li>🌐 <strong>Azure VM Deployment</strong></li>
    <li>🧪 <strong>Flask-based Web Services</strong></li>
    <li>⚖️ <strong>Weighted Random Selection Algorithm</strong></li>
    <li>📊 <strong>Dynamic load-aware traffic distribution</strong></li>
    <li>🔧 <strong>Live system stress metric fetching</strong></li>
    <li>📈 <strong>Scalable and maintainable microservice design</strong></li>
  </ul>

  <h2>⚙️ Architecture in Action</h2>
  <p>The system includes:</p>
  <ul>
    <li>🧱 Three Flask-based Web Servers</li>
    <li>🔁 One Python-based Load Balancer</li>
    <li>🕸️ All linked in a Docker Compose network</li>
  </ul>
  <p>Each incoming request is:</p>
  <ol>
    <li>📥 Received by the load balancer.</li>
    <li>📊 Stress values (CPU, RAM) are fetched.</li>
    <li>⚖️ Adjusted weights are computed.</li>
    <li>🎯 A backend server is chosen smartly.</li>
    <li>🔁 Response is forwarded back to the client.</li>
  </ol>

  <h2>📦 How to Run</h2>
  <pre><code># Clone the repo
git clone https://github.com/your-username/adaptive-load-balancer.git
cd adaptive-load-balancer

# Build and run containers
docker-compose up --build
</code></pre>
  <p>Then open your browser and visit:</p>
  <ul>
    <li>📍 <code>http://&lt;your-azure-vm-ip&gt;</code></li>
    <li>📍 <code>http://&lt;your-azure-vm-ip&gt;/metrics</code> to view stress</li>
  </ul>

  <h2>📉 Example: Dynamic Load Distribution</h2>

  <h4>Low Stress Scenario</h4>
  <table>
    <tr>
      <th>Server</th>
      <th>Original Weight</th>
      <th>Adjusted Weight</th>
    </tr>
    <tr>
      <td>Server1</td>
      <td>3</td>
      <td>2.4</td>
    </tr>
    <tr>
      <td>Server2</td>
      <td>2</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td>Server3</td>
      <td>2</td>
      <td>1.6</td>
    </tr>
  </table>

  <h4>High Stress Scenario</h4>
  <table>
    <tr>
      <th>Server</th>
      <th>Original Weight</th>
      <th>Adjusted Weight</th>
    </tr>
    <tr>
      <td>Server1</td>
      <td>3</td>
      <td>1.71</td>
    </tr>
    <tr>
      <td>Server2</td>
      <td>2</td>
      <td>1.14</td>
    </tr>
    <tr>
      <td>Server3</td>
      <td>2</td>
      <td>1.14</td>
    </tr>
  </table>

  <h2>✅ Status</h2>
  <ul>
    <li>✅ Dockerized Flask microservices</li>
    <li>✅ Load Balancer with Weighted Random Selection</li>
    <li>✅ Real-time stress monitoring and adaptive traffic routing</li>
    <li>✅ Fully working on Azure VM</li>
  </ul>

  <h2>💡 Conclusion</h2>
  <p>This Adaptive Load Balancer is perfect for:</p>
  <ul>
    <li>📘 Learning about <strong>SDN and cloud-native architectures</strong></li>
    <li>📗 Building scalable microservice systems</li>
    <li>📕 Enhancing fault tolerance and performance</li>
  </ul>
  <blockquote><em>“Balance is not something you find, it’s something you create… with Python and Docker.” 🧘‍♀️🐍🐳</em></blockquote>

  <h2>👨‍💻 Authors</h2>
  <ul>
    <li><strong>Prudhvi Ponnada</strong>: ponnadaprudhvi18@gmail.com</li>
    <li><strong>Sai Siri Sree Venturi</strong>: s3.venturi@gmail.com</li>
  </ul>

  <h2>📬 Contribute</h2>
  <p>Want to contribute or have suggestions? Fork this repo or open an issue!</p>
</body>
</html>
