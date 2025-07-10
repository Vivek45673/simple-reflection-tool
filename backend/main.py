from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow CORS for local frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReflectionRequest(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_emotion(request: ReflectionRequest):
    # Mock analysis
    return {
        "emotion": "Anxious",
        "confidence": 0.85
    }