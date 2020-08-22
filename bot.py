import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import re

vk = vk_api.VkApi(token="919e919e3815b66463acace0ec808f8e88d010e3e2863477fb93d1542a70cdc48245ee3622e9318f7320c")
longpoll = VkBotLongPoll(vk, '197891905')
vk = vk.get_api()
_eng_chars = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
_rus_chars = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"
_trans_table = dict(zip(_eng_chars, _rus_chars))

def fix_layout(s):
    return u''.join([_trans_table.get(c, c) for c in s])
print("Бот запущен")

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            request = event.object.message['text'].lower()
            peer_ida = event.object.message['peer_id']
            reply = event.object.message['date']
            linka = event.object.message['attachments']
            razbit = request.replace(',','').split(' ')
            #for i in razbit:
                #if i != '' and i[:4] != 'http':
                    #if re.search(r'[a-z]',i) != None:
                        #vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = fix_layout(request))
                        #break
            if request == "физфак":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Чемпион")
            if request == "лучший в спбгу":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "факультет физический, кто идет в ПМПУ тот пидр венерический!")
            for i in razbit:
                if i == "бот":
                    vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Нет, блять, не бот")
            if request == "слава иванову":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Слава матану")
            if request == "аве иванову":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Аве матану")
            if request == "аве иванов":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Аве матану")
            if request == "ave иванову":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Ave матану")
            if request == "ave иванов":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Ave матану")
            for i in razbit:
                if i == "ансис" or i == "ансису" or i == "ансисом" or i == "ансиса" or i == "ansys":
                    vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Забудь нахуй")
            if request == "что делать с матаном?":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Иди ботай")
            if request == "*получил зачет*":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Пива этому господину")