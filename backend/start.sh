#!/bin/bash
echo "Starting application..."
echo "PORT: $PORT"
echo "DATABASE_URL: ${DATABASE_URL:0:20}..." # Only show first 20 chars for security

uvicorn main:app --host 0.0.0.0 --port $PORT --timeout-keep-alive 75 