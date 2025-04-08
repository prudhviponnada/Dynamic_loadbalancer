# Use an official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the load balancer script into the container
COPY loadbalancer.py /app/loadbalancer.py

# Install dependencies
RUN pip install flask requests psutil

# Expose the required port
EXPOSE 8080

# Run the load balancer script
CMD ["python", "/app/loadbalancer.py"]

