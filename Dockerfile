# Web Server Dockerfile Server 1 server 2 server 3
FROM python:3.9-slim
WORKDIR /app
COPY app.py .
# Install Flask and psutil
RUN pip install flask psutil
RUN apt-get update && apt-get install -y stress
CMD ["python", "app.py"]