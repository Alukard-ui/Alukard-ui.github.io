# *- coding: utf-8 -*

from random import choice
from nltk import edit_distance

class Chatter:

    def __init__(self,content):
        self.config = content
        zfile = zipfile.ZipFile('dialogues.zip', 'r')  # open file
        for filename in zfile.namelist():
            zfile.extract(filename)
        with open('dialogues.txt', 'r', encoding='utf-8') as file:
            contents = file.read()
        dialogues_str = contents.split('\n\n')
        self.dialogues = [dialogues_str.split('\n')[:2] for dialogues_str in dialogues_str]
        self.dialogues_filter = []


    def filter_text(self,text):
        text = text.lower()
        text =[c for c in text if c in 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя- ']
        text = ''.join(text)
        return text

    def filter_phrase(self,text):
        text = text.lower
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя- '
        result= ''.join([c for c in text if c in alphabet])
        return result

    def dialogues_response(self):
        questions = set()
        for dialogues in self.dialogues:
            if len(dialogues) !=2:
                continue
            question, answer = dialogues
            question = question[2:]
            question = self.filter_text(question)
            answer = answer[2:]
            if question !='' and question not in questions:
                questions.add(question)
                self.dialogues_filter.append([question,answer])

    def get_intent(self, question):
        for intent, intent_data in self.config['intents'].items():
            for example in intent_data['examples']:
                dist = edit_distance(self.filter_text(example),self.filter_text(question))
                if dist/len(example) < 0.4:
                    return intent

    def get_answer_by_intent(self, intent):
        if intent in self.config['intents']:
            return choice(self.config['intents'][intent]['responses'])

    def generate_answer_by_text(self, replica):
        replica = self.filter_text(replica)
        for question,answer in self.dialogues_filter:
            dist = edit_distance(replica, question)
            if dist / len(question) < 0.2:
                return answer

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


# Chatter = Chatter()
# question =input()
# while question not in ['выход','exit']:
#     answer=Chatter.Responce(question)
#     print(answer)
#     question=input()
# question = str(input())
# while question not in ['выход','х']:
#     question = str(input())
#     answer = Responce(question)
#     print(answer)