# Minimal FastAPI app with CORS
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://uberjoker.github.io", "http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Accept"],
    max_age=3600,
)

@app.get("/")
def root():
    return {"status": "healthy"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/log_meal/")
def log_meal():
    return {"message": "Meal logged successfully!", "id": 1} 