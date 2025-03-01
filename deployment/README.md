# AI Nutrition Assistant

## 🚀 Setup Instructions

### 1️⃣ Install Dependencies (Backend)
Run the following command inside the `backend/` directory:
```bash
pip install -r requirements.txt
```

### 2️⃣ Start the FastAPI Server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 3️⃣ Set Up the Database (PostgreSQL)
```bash
psql -U username -d dbname -f database/init.sql
```

### 4️⃣ Open the Web Interface
- Open `frontend/index.html` in a browser.
- Enter meal details and click "Submit".

### 🌐 Deploying to Cloud
#### **Option 1: Deploy Backend to Render (Free)**
1. Create an account at [https://render.com](https://render.com).
2. Deploy FastAPI using **Render's Web Service**.
3. Set `DATABASE_URL` in the environment variables.

#### **Option 2: Deploy Frontend on Netlify**
1. Create an account at [https://www.netlify.com](https://www.netlify.com).
2. Drag & drop the `frontend/` folder to Netlify.
3. Set backend API URL (`http://your-backend-url.onrender.com`).

Happy coding! 🚀
