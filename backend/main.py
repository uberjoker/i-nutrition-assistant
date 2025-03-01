from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Nutrition Assistant API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://uberjoker.github.io", "http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Accept"],
    max_age=3600,
)

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    try:
        return psycopg2.connect(DATABASE_URL)
    except Exception as e:
        print(f"Database connection error: {e}")
        raise HTTPException(status_code=500, detail="Database connection error")

# Initialize database tables
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS meal_logs (
                id SERIAL PRIMARY KEY,
                timestamp TIMESTAMP NOT NULL,
                meal_description TEXT NOT NULL,
                blood_sugar FLOAT,
                medication TEXT,
                calories INTEGER,
                carbs FLOAT,
                protein FLOAT,
                fat FLOAT,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
    except Exception as e:
        print(f"Database initialization error: {e}")
        raise HTTPException(status_code=500, detail="Database initialization error")
    finally:
        cursor.close()
        conn.close()

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    init_db()

class MealLog(BaseModel):
    timestamp: str
    meal_description: str
    blood_sugar: float | None = None
    medication: str | None = None
    calories: int | None = None
    carbs: float | None = None
    protein: float | None = None
    fat: float | None = None
    notes: str | None = None

@app.post("/log_meal/")
def log_meal(data: MealLog):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Debug logging
        print(f"Received data: {data}")
        print(f"Calories type: {type(data.calories)}, value: {data.calories}")
        print(f"Carbs type: {type(data.carbs)}, value: {data.carbs}")
        print(f"Protein type: {type(data.protein)}, value: {data.protein}")
        print(f"Fat type: {type(data.fat)}, value: {data.fat}")
        
        cursor.execute("""
            INSERT INTO meal_logs 
            (timestamp, meal_description, blood_sugar, medication, calories, carbs, protein, fat, notes)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (
            data.timestamp,
            data.meal_description,
            data.blood_sugar,
            data.medication,
            data.calories,
            data.carbs,
            data.protein,
            data.fat,
            data.notes
        ))
        meal_id = cursor.fetchone()[0]
        conn.commit()
        return {"message": "Meal logged successfully!", "id": meal_id}
    except Exception as e:
        conn.rollback()
        print(f"Error logging meal: {e}")
        raise HTTPException(status_code=500, detail=f"Error logging meal: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@app.get("/meals/")
def get_meals():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT * FROM meal_logs 
            ORDER BY timestamp DESC 
            LIMIT 100
        """)
        columns = [desc[0] for desc in cursor.description]
        meals = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return meals
    except Exception as e:
        print(f"Error fetching meals: {e}")
        raise HTTPException(status_code=500, detail="Error fetching meals")
    finally:
        cursor.close()
        conn.close()

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}
