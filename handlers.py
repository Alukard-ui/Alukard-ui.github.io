# *- coding: utf-8 -*

import re
from models import LaboratoryWork
from pony.orm import db_session
import random

re_number = re.compile(r'№([0-9]{1,4})')
re_class = re.compile(r'[1-4]{1}')

def handler_numberLab(text,context):
    find = re.findall(re_number,text)
    if find:
        context['numberLab'] = find[0]
        return True
    else:
        return False

def handler_class(text,context):
    find = re.findall(re_class,text)
    if find:
        context['class'] = find[0]
        return True
    else:
        return False

@db_session
def handler_link(text,context):
    id=context['class']+context['numberLab']
    laba = LaboratoryWork.get(id=id)
    context['oldPiggyBank'] = laba.oldPiggyBank
    context['newPiggyBank'] = laba.newPiggyBank
    context['IOFPiggyBank'] = laba.IOFPiggyBank
    return text.lower() == 'да'



def group_handler_laboratory_work(text):
    find = re.findall(re_number,text)
    numberLab = LaboratoryWork.get(id=find[0])
    if numberLab:
        old = numberLab.oldPiggyBank
        new = numberLab.newPiggyBank
        IOF = numberLab.IOFPiggyBank
        text = f'{old} - копилка стариков\n' \
               f'{new} - копилка\n' \
               f'{IOF} - копилка №2'
    return text


def group_handler_anecdote(text):
    with open('aneki.txt','r',encoding='utf-8') as file:
        anek = file.read().split('/')
        chose_anek = random.choice(anek)
    return chose_anek