import asyncio

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse

from backend.LLM import ClaudeBase
from backend.Langchain_claude import ClaudeLangchain

# LLM
claude = ClaudeBase()
streaming_claude = ClaudeLangchain()

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

# 🔥 Streaming endpoint
@app.post("/chat-stream")
async def chat_stream(message: Message):

    async def event_generator():
        response = streaming_claude.get_basic_streaming_response(message.text)

        for chunk in response:
            if chunk.content:
                yield {
                    "event": "message",
                    "data": chunk.content
                }
                await asyncio.sleep(0.01)  # smooth streaming

    return EventSourceResponse(event_generator())