import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import re
import datetime

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
            #for i in razbit:
             #   if i == "бот":
              #      vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Нет, блять, не бот")
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
                if i == "ансис" or i == "ансису" or i == "ансисом" or i == "ансиса" or i == "ansys" or i == "ансисов":
                    vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Забудь нахуй")
            if request == "что делать с матаном?":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Иди ботай")
            if request == "кураторы":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = "Пора познакомить вас с вашими кураторами, к которым вы можете обращаться по интересующим вопросам."
                                                                                           "Распределение на группы (для всех кроме радиофизики (Электрочто-то там) и ИОФ) произойдет в начале семестра.\n"
                                                                                           "Б.01 (радиофизика) - Инсаф Нуреев (3 курс)\n"
                                                                                           "Б.02 (физика, база) - Полина Малова (3 курс), Дмитрий Гранкин (3 курс)\n"
                                                                                           "Б.03 (физика) - Иван Фоломеев (3 курс)\n"
                                                                                           "Б.04 (физика) - Варя Кубенко (4 курс)\n"
                                                                                           "Б.05 (физика,ципс) - Лёша Клочай (2 курс), Вячеслав Кривороль (5 курс)\n"
                                                                                           "Б.06 (пмф) - Даниил Усов (5 курс), Тимур Катунов (2 курс)\n"
                                                                                           "Б.07 (пмф) - Илья Козлов (3 курс), Влад Панов (3 курс)\n"
                                                                                           "Б.20 (иоф) - Алексей Раев (2 курс), Александр Семёнов (2 курс)\n"
                                                                                           "По общим вопросам - Лиза Тельная (6 курс), Аня Карчевская (3 курс)\n"
                                                                                           "Куратор иностранных обучающихся ФФ - Тосио Наганава (3 курс)"
                                                                                           "Не бойтесь задавать вопросы, мы будем рады помочь освоиться в новой для вас среде😊")
            if request == "лаба 1":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/001.%20Измерение%20длины%2C%20объёма%20и%20плотности/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/1\n-копилка ИОФ\n"
                                                                                                   "https://yadi.sk/d/VGymqWhp0uV44Q/_ЛАБЫ/1%20сем/001.Измерение%20длины%2C%20объема%20и%20плотности%20твёрдых%20тел%20с\n"
                                                                                                   "-общая копилка")