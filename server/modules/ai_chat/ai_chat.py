from typing import Optional

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from server.prompts.ai_chat_prompts import ai_chat_prompts
from server.utils.filter_text import filter_text_using_regex
from server.utils.openai_model import get_text_from_openai

ai_chat_generation = APIRouter()

@ai_chat_generation.post("/ai_chat_generator")
def ai_chat_generator(request: Optional[list]):
    try:
        if not request:
            raise KeyError("text not found.")

        else:
            raw_text = request[0]

            # remove bullets, numbers, etc.. from text
            # text = filter_text_using_regex(text=raw_text)
            prompt = ai_chat_prompts(text=raw_text)

            # gpt-generated completion
            gpt_generated_text = get_text_from_openai(
                prompt=prompt, temperature=1, max_tokens=3000
            )
            response = {
                "status_code": 200,
                "message": "Lesson was Generated Successfully.",
                "data": gpt_generated_text,
            }

    except Exception as e:
        response = {
            "status_code": 500,
            "message": f"run time error in module generation with reason: {e}",
            "data": None,
        }

    return JSONResponse(content=response)
