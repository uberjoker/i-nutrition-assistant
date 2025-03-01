from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

class MealLog(BaseModel):
    timestamp: str
    meal_description: str
    blood_sugar: float
    medication: str

@app.post("/log_meal/")
def log_meal(data: MealLog):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO meal_logs (timestamp, meal_description, blood_sugar, medication) VALUES (%s, %s, %s, %s)",
                   (data.timestamp, data.meal_description, data.blood_sugar, data.medication))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Meal logged successfully!"}

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}
