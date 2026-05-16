import asyncio

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse

from backend.LLM import ClaudeBase
from backend.Langchain_claude import ClaudeLangchain
from backend.claude_with_agent import ClaudeLangchainAgent

# LLM
claude = ClaudeBase()
streaming_claude = ClaudeLangchain()
agent_lc_claude = ClaudeLangchainAgent()
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

@app.post("/chat-stream")
def chat_stream(message: Message):
    print("message.text : ",message.text)
    response = agent_lc_claude.get_basic_streaming_response(message.text)
    print("response:", response)
    return {"response": response} if response else {"response": None}


# @app.post("/chat-stream")
# async def chat_stream(message: Message):
#
#     async def event_generator():
#         response = streaming_claude.get_basic_streaming_response(message.text)
#
#         for i, chunk in enumerate(response):
#             print("i : ",i,"chunk : ", chunk)
#             if not chunk.content:
#                 continue
#
#             content = chunk.content
#
#             if isinstance(content, list):
#                 text = "".join(block.get("text", "") for block in content if isinstance(block, dict))
#             elif isinstance(content, str):
#                 text = content
#             else:
#                 text = ""
#
#             if text:
#                 yield f"{text}\n\n"
#                 await asyncio.sleep(0.01)
#
#     return EventSourceResponse(event_generator())
