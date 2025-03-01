# AI Nutrition Assistant

A web application to track meals, blood sugar levels, and medication.

## Features

- Log meals with timestamps
- Track blood sugar levels
- Record medication intake
- Mobile-friendly interface

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: FastAPI (Python)
- Database: PostgreSQL

## Local Development

1. Install Python 3.11+ and PostgreSQL
2. Clone this repository
3. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```bash
   psql -f database/init.sql
   ```
5. Start the backend:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
6. Open frontend/index.html in your browser

## Deployment

The application is deployed using:
- Backend: Fly.io
- Frontend: GitHub Pages
- Database: Fly PostgreSQL

### Backend Deployment (Fly.io)

1. Install Fly CLI
2. Login to Fly:
   ```bash
   fly auth login
   ```
3. Deploy:
   ```bash
   cd backend
   fly launch
   fly postgres create
   fly postgres attach
   fly deploy
   ```

### Frontend Deployment (GitHub Pages)

The frontend is automatically deployed to GitHub Pages when changes are pushed to the main branch.
