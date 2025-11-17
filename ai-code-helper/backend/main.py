from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import google.generativeai as genai
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="AI Code Helper API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

class CodeRequest(BaseModel):
    code: str
    language: str = "python"
    task: str = "explain"

class ExplanationRequest(BaseModel):
    concept: str
    level: str = "beginner"

def call_gemini(prompt):
    """Call Google Gemini API for AI responses"""
    try:
        model = genai.GenerativeModel('models/gemini-2.0-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        logger.error(f"Error calling Gemini: {str(e)}")
        return f"I apologize, but the AI service is currently unavailable. Error: {str(e)}"

@app.get("/")
async def root():
    return {"message": "AI Code Helper API", "status": "running", "ai_provider": "Google Gemini"}

@app.post("/api/code/explain")
async def explain_code(request: CodeRequest):
    prompt = f"Explain this {request.language} code: {request.code}"
    explanation = call_gemini(prompt)
    return JSONResponse({"success": True, "explanation": explanation})

@app.post("/api/code/debug")
async def debug_code(request: CodeRequest):
    prompt = f"Debug this {request.language} code: {request.code}"
    debug_info = call_gemini(prompt)
    return JSONResponse({"success": True, "debug_info": debug_info})

@app.post("/api/code/translate")
async def translate_code(request: CodeRequest):
    prompt = f"Translate this code to {request.language}: {request.code}"
    translation = call_gemini(prompt)
    return JSONResponse({"success": True, "translation": translation})

@app.post("/api/concept/explain")
async def explain_concept(request: ExplanationRequest):
    prompt = f"Explain {request.concept} at {request.level} level"
    explanation = call_gemini(prompt)
    return JSONResponse({"success": True, "explanation": explanation})

@app.post("/api/code/optimize")
async def optimize_code(request: CodeRequest):
    prompt = f"Optimize this {request.language} code: {request.code}"
    optimization = call_gemini(prompt)
    return JSONResponse({"success": True, "optimization": optimization})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)