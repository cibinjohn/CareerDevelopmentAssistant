from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from backend.LLM import ClaudeBase

# LLM
claude = ClaudeBase()

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.post("/chat")
def chat(message: Message):
    user_input = message.text

    llm_output = claude.get_basic_response(user_input)

    # For now: just echo
    return {
        "response": f"{llm_output}"
    }