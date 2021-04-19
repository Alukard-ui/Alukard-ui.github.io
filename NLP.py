# *- encoding: utf-8 -*

from random import choice
from nltk import edit_distance


class Chatter():

    def __init__(self,content):
        self.config = content

    def filter_text(self,text):
        text = text.lower()
        text =[c for c in text if c in 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя- ']
        text = ''.join(text)
        return text

    def get_intent(self, question):
        for intent, intent_data in self.config['intents'].items():
            for example in intent_data['examples']:
                dist = edit_distance(self.filter_text(example),self.filter_text(question))
                if dist/len(example) < 0.4:
                    return intent

    def get_answer_by_intent(self, intent):
        if intent in self.config['intents']:
            return choice(self.config['intents'][intent]['response'])
        return

    def generate_answer_by_text(self, question):
        return

    def get_failure_phrase(self):
        phrase = self.config['failure_phrases']
        return choice(phrase)

    def Responce(self,question):
        # NLU
        intent = self.get_intent(question)
        # Get answer

        # Find ready answer
        if intent:
            answer = self.get_answer_by_intent(intent)
            if answer:
                return answer
        # Generate approach based on the context answer
        answer = self.generate_answer_by_text(question)
        if answer:
            return answer

        # Use stub
        answer = self.get_failure_phrase()
        return answer


Chatter = Chatter()
question =input()
while question not in ['выход','exit']:
    answer=Chatter.Responce(question)
    print(answer)
    question=input()
# question = str(input())
# while question not in ['выход','х']:
#     question = str(input())
#     answer = Responce(question)
#     print(answer)
