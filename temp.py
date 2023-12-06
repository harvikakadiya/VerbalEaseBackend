# from langdetect import detect

# sentence = "Tanzania ni nchi inayoongoza kwa utalii barani afrika"

# print(detect(sentence))

# pip install -U deep-translator

from deep_translator import GoogleTranslator

temp = GoogleTranslator(source='auto', target='en').translate("guten Tag")
GoogleTranslator()
print(temp)