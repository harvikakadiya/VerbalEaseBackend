from typing import Optional

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from server.prompts.translate_text_prompts import translate_text_prompts
from server.utils.filter_text import filter_text_using_regex
from server.utils.openai_model import get_text_from_openai

translate_text_generation = APIRouter()

@translate_text_generation.post("/translate_text_generator")
def translate_text_generator(request: Optional[dict]):
    try:
        if not request:
            raise KeyError("topic key not found.")

        else:
            course = request["course"]
            topic_list = request["topic"].split("\n")

            lesson_dictionary = []

            if not course:
                raise KeyError("course name not found in request.")
            elif len(topic_list) == 0:
                raise KeyError("subtopic list is empty.")

            for topic in topic_list:
                # remove bullets, numbers, etc.. from text
                topic = filter_text_using_regex(text=topic)
                course = filter_text_using_regex(text=course)
                prompt = translate_text_prompts(course=course, topic=topic)

                # gpt-generated completion
                gpt_generated_text = get_text_from_openai(
                    prompt=prompt, temperature=1, max_tokens=300
                )

                # split results
                result = [data.strip() for data in gpt_generated_text.split("\n") if data]
                lesson_dictionary.append(
                    {"prompt": {"course": course, "topic": topic}, "completion": result}
                )

            response = {
                "status_code": 200,
                "message": "Lesson was Generated Successfully.",
                "data": lesson_dictionary,
            }

    except Exception as e:
        response = {
            "status_code": 500,
            "message": f"run time error in module generation with reason: {e}",
            "data": None,
        }

    return JSONResponse(content=response)
