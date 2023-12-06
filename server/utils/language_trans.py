from deep_translator import GoogleTranslator

def text_translate(text, to_lang):
    translated_text = GoogleTranslator(source='auto', target=to_lang).translate(text)
    return translated_text

# from googletrans import Translator  # pip install googletrans==4.0.0-rc1

# # Initialize the Translator
# translator = Translator()

# # Language detector
# def language_detector(text):
#     result = translator.detect(text).lang
#     return result

# # Language translator
# def text_translate(text, from_language, to_language):
#     result =  translator.translate(text, src=from_language, dest=to_language).text
#     return result
