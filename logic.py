from translate import Translator
from collections import defaultdict

questions = {'what is your name' : "I'm a super cool bot and my purpose is to help you!",
             "how old are you" : "That's too philosophical of a question..."}

class TextAnalysis():
    
    memory = defaultdict(list)

    def __init__(self, text, owner):

        TextAnalysis.memory[owner].append(self)

        self.text = text
        self.translation = self.__translate(self.text, "en", "es")

        if self.text in questions.keys():
            self.response = questions[self.text]
        else:
            self.response = self.get_answer() 

    
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "es")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            translator = Translator(from_lang=from_lang, to_lang=to_lang)
            translation = translator.translate(text)
            return translation
        except:
            return "Translation failed"
