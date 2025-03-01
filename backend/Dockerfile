# Use Python 3.9 slim image
FROM python:3.9-slim

# Install debugging tools
RUN apt-get update && apt-get install -y procps curl && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Make start script executable
RUN chmod +x start.sh

# Set environment variables
ENV PORT=8080

# Expose the port
EXPOSE 8080

# Run the application with startup script
CMD /bin/bash ./start.sh 