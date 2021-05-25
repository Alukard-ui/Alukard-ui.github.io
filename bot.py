# *- coding: utf-8 -*


"""
:authors:
"""
import random
import logging
import re
import logging.config
import _logging_settings
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import settings
from models import UserState,LaboratoryWork
import handlers
from pony.orm import db_session


logging.config.dictConfig(_logging_settings.log_config)
log = logging.getLogger('bot')

class Bot:
    def __init__(self,group_id,token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk,self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception as err:
                log.exception("Ошибка обработки")

    @db_session
    def on_event(self,event):
        if event.type != VkBotEventType.MESSAGE_NEW:
            return
        user_id = event.object.message['peer_id']
        text = event.object.message['text']
        if int(user_id)-2*10**9<0:
            state = UserState.get(user_id=str(user_id))
            if state is not None:
                text_to_send = self.continue_scenario(text=text,state=state)
            else:
                for intent in settings.INTENTS:
                    if any(token in text.lower() for token in intent['tokens']):
                        if intent['answer']:
                            text_to_send = intent['answer']
                        else:
                            text_to_send = self.start_scenario(user_id, intent['scenario'])
                        break
                else:
                    text_to_send = settings.DEFAULT_ANSWER
            self.send_message(text_to_send, user_id)
        else:
            for intent in settings.INTENTS:
                if any(token in text.lower() for token in intent['tokens']):
                    if intent['answer']:
                        text_to_send = intent['answer']
                        self.send_message(text_to_send, user_id)
                    if intent['group_handler']:
                        handler = getattr(handlers,intent['group_handler'])
                        text_to_send = handler(text)
                        if text_to_send:
                            self.send_message(text_to_send,user_id)




    def start_scenario(self, user_id, scenario_name):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        first_name = self.get_user_info(user_id)[0]['first_name']
        last_name = self.get_user_info(user_id)[0]['last_name']
        UserState(user_id=str(user_id),scenario_name=scenario_name, step_name=first_step,
                  context={'first_name':first_name,'last_name':last_name})
        return text_to_send

    def continue_scenario(self, text,state):
        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]
        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):
            next_step = steps[step['next_step']]
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                state.step_name = step['next_step']
            else:
                state.delete()
        else:
            text_to_send = step['failure_text']
        return text_to_send

    def get_user_info(self,user_id):
        return self.vk.method('users.get', {'user_ids':user_id})

    def send_message(self,text,user_id=None):
        self.api.messages.send(
            message=text,
            random_id=random.randint(0, 2 ** 20),
            peer_id=user_id,
        )

if __name__ == "__main__":
    bot = Bot(settings.group_id,settings.token)
    bot.run()