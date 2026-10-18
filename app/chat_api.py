from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Figma React AI Agent",
    description="Conversational API for the Figma to React AI Agent",
    version="1.0.0"
)

# React frontend will run on localhost:5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
def root():
    return {
        "message": "Figma React AI Agent API is running"
    }


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    user_message = request.message

    # Temporary response.
    # Later this will call your actual agent.
    response = f"Agent received: {user_message}"

    return ChatResponse(
        response=response
    )