import os

import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Openai completion API call for davinci model.
def get_text_from_openai(
    prompt, max_tokens=3000, temperature=1, frequency_penalty=0.5, presence_penalty=0.5
):
    try:
        gpt_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "user",
                "content": str(prompt)
                }
            ],
            temperature=1,
            max_tokens=250,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["###"]
        )
        response = gpt_response.choices[0].message.content
        return response
    except Exception as e:
        raise Exception(f"model failure with reason: {e}")
