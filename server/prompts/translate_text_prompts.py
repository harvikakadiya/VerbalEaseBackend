# this file contains prompts for translator


def translate_text_prompts(lang, text):
    return f"""Translate the given text to given language: 
    text: {text},
    language: {lang}"""