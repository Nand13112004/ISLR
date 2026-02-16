from googletrans import Translator, LANGUAGES

class TextTranslator:
    def __init__(self):
        self.translator = Translator()
        self.languages = LANGUAGES
        self.language_names = list(LANGUAGES.values())

    def get_language_code(self, lang_name):
        for code, name in self.languages.items():
            if name.lower() == lang_name.lower():
                return code
        raise ValueError(f"Language '{lang_name}' not found.")

    def translate(self, text, lang_name):
        if not text.strip():
            return ""
        lang_code = self.get_language_code(lang_name)
        translation = self.translator.translate(text, dest=lang_code)
        return translation.text
