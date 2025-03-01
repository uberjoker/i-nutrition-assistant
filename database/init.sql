CREATE TABLE IF NOT EXISTS meal_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    meal_description TEXT,
    blood_sugar FLOAT,
    medication TEXT
);
