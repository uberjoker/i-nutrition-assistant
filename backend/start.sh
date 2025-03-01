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
exec uvicorn main:app --host 0.0.0.0 --port $PORT --log-level debug 