from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.analyzer import analyze_text

app = FastAPI(title="AI Communication Intelligence Platform")

# ✅ CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "API is running"}

@app.post("/analyze")
def analyze(payload: dict):
    text = payload.get("text", "")
    return analyze_text(text)
