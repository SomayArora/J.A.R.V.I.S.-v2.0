from googletrans import Translator

def translate_to_english(text):
    """Translate the given text to English."""
    translator = Translator()
    try:
        translated = translator.translate(text, dest='en')
        return translated.text.lower()
    except Exception as e:
        print("Translation error:", e)
        return text.lower()

print(translate_to_english("merhaba"))

