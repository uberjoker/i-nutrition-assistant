#!/bin/bash
set -e  # Exit on error

echo "Starting application..."
echo "Current directory: $(pwd)"
echo "Files in current directory:"
ls -la

echo "Environment variables:"
echo "PORT: $PORT"
echo "DATABASE_URL exists: $(if [ -n "$DATABASE_URL" ]; then echo "yes"; else echo "no"; fi)"

echo "Python version:"
python --version

echo "Starting uvicorn..."
# Start uvicorn in the background
uvicorn main:app --host 0.0.0.0 --port $PORT --log-level debug &
PID=$!

# Wait for the server to be ready
echo "Waiting for server to be ready..."
for i in {1..30}; do
  if curl -s http://localhost:$PORT/health > /dev/null; then
    echo "Server is ready!"
    # Keep the script running
    wait $PID
    exit 0
  fi
  echo "Attempt $i: Server not ready yet..."
  sleep 1
done

echo "Server failed to start within 30 seconds"
exit 1 