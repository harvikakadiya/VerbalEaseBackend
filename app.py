from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from server.modules.paraphraser.paraphraser import paraphrase_text_generation
from server.modules.summarizer.summarizer import summarize_text_generation
from server.modules.translator.translator import translate_text_generation
from server.modules.ai_chat.ai_chat import ai_chat_generation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    paraphrase_text_generation, tags=["Pharaphrase Text"], prefix="/pharaphrase-Text-system/v1"
)
app.include_router(
    summarize_text_generation, tags=["Summarize Text"], prefix="/summarize-Text-system/v1"
)
app.include_router(
    translate_text_generation, tags=["Translate Text"], prefix="/translate-Text-system/v1"
)
app.include_router(
    ai_chat_generation, tags=["AI Chat Text"], prefix="/ai-chat-system/v1"
)

@app.get("/")
def home():
    return {"message": "Welcome to VerbalEase."}
