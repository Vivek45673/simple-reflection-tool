# Simple Emotion Reflection Tool

A mobile-first web app where users enter a short text reflection, which is sent to a Python FastAPI backend for mock emotion analysis, and the frontend displays the result cleanly.

## 🚀 Features
- TypeScript + Next.js frontend
- FastAPI backend
- Clean form submission and display of emotion analysis
- Loading and error state handling

## 📦 Setup Instructions

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install fastapi uvicorn
uvicorn main:app --reload --port 8000
