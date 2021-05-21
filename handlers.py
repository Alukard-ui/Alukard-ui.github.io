# *- coding: utf-8 -*

import re
from models import LaboratoryWork
from pony.orm import db_session

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