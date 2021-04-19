import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import re
import datetime
import requests
import random
from bs4 import BeautifulSoup
import bot_config
from NLP import Chatter

HOST = 'https://timetable.spbu.ru/'
URLiof = 'https://timetable.spbu.ru/PHYS/StudentGroupEvents/Primary/276857/'
URL20B006 = 'https://timetable.spbu.ru/PHYS/StudentGroupEvents/Primary/276325/'
URLiof2020='https://timetable.spbu.ru/PHYS/StudentGroupEvents/Primary/298316/'
data = '2020-09-07'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.206'
}

def get_html(url,params=''):
    r = requests.get(url+params.strftime('%Y-%m-%d'),headers = HEADERS)
    return r

def get_content(html):
    soup = BeautifulSoup(html,'lxml')
    xz = []
    items = soup.find_all("div", class_ ="panel panel-default")
    for item in items:
        xz.append( " ".join(item.text.split()))
    return xz

def ras(URL,xz,ret):
                for i in range(30):
                    if ret == xz:
                        html = get_html(URL,xz)
                        vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message =get_content(html.text)[2])
                        break
                    elif  ret > xz:
                        xz += datetime.timedelta(days=7)
                    else:
                        xz -= datetime.timedelta(days=7)
                        html = get_html(URL,xz)
                        wq=ret.day-xz.day
                        if wq == 6:
                            vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message ="Воскресенье идиот")
                        else:
                            vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message =get_content(html.text)[wq+2])
                            break

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
    xz = datetime.date(year=2020, month=8, day=31)
    ret = datetime.date.today()
    Chatter = Chatter(content=bot_config.init)
    Chatter.dialogues_response()
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
            if request == "слава лоли":
                vk.messages.send(random_id=get_random_id(), peer_id=peer_ida, message="Смерть лоликонщикам")
                while request not in ['все хватит','выход']:
                    for event in longpoll.listen():
                        if event.type == VkBotEventType.MESSAGE_NEW:
                            request = event.object.message['text'].lower()
                            peer_ida = event.object.message['peer_id']
                            reply = event.object.message['date']
                            linka = event.object.message['attachments']
                            vk.messages.send(random_id=get_random_id(), peer_id=peer_ida, message=Chatter.Responce(request))
                            if request in ['выход','exit']:
                                break
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
                if i == ("ансис" or i == "ансису" or i == "ансисом" or i == "ансиса" or i == "ansys" or i == "ансисов") and random.random()<=0.1:
                    vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Забудь нахуй")
            if request == "что делать с матаном?":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Иди ботай")
            for i in razbit:
                if i == ("ансис" or i == "ансису" or i == "ансисом" or i == "ансиса" or i == "ansys" or i == "ансисов") and random.random()<=0.1:
                     vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Да поможет тебе Бог(Аня)")
            for i in razbit:
                if i == ("ансис" or i == "ансису" or i == "ансисом" or i == "ансиса" or i == "ansys" or i == "ансисов") and random.random()<=0.1:
                     vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "https://www.ansys.com")
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
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/1\n-копилка 2\n"
                                                                                                   "https://yadi.sk/d/VGymqWhp0uV44Q/_ЛАБЫ/1%20сем/001.Измерение%20длины%2C%20объема%20и%20плотности%20твёрдых%20тел%20с\n"
                                                                                                   "-общая копилка")
            if request == "лаба 2":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/001.%20Измерение%20длины%2C%20объёма%20и%20плотности/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/002\n-копилка 2\n"
                                                                                                   "https://yadi.sk/d/VGymqWhp0uV44Q/_ЛАБЫ/1%20сем/002.Изучение%20упругих%20свойств%20спиральной%20пружины%20и%20тонкой%20пластины\n"
                                                                                                   "-общая копилка")

            if request == "лаба 3":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/003.%20Гидростатическое%20взвешивание/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/003\n-копилка 2\n"
                                                                                                   "https://yadi.sk/d/VGymqWhp0uV44Q/_ЛАБЫ/1%20сем/003.Определение%20плотности%20тела%20способом%20гидростатического%20взвешивания\n"
                                                                                                   "-общая копилка")
            if request == "лаба 4":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/004.%20Случайные%20ошибки/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/004\n-копилка 2\n"
                                                                                                   "https://yadi.sk/d/VGymqWhp0uV44Q/_ЛАБЫ/1%20сем/004.Случайные%20ошибки\n"
                                                                                                   "-общая копилка")
            if request == "лаба 5":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/005.%20Прецессия%20и%20нутация/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/005\n-копилка 2\n"
                                                                                                   "https://yadi.sk/d/VGymqWhp0uV44Q/_ЛАБЫ/1%20сем/005.Прецессия%20и%20нутация\n"
                                                                                                   "-общая копилка")
            if request == "лаба хз":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nхз\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "хз\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 6":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/006.%20Торсионный%20осциллятор/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/006\n-копилка 2\n"
                                                                                                   "https://yadi.sk/d/VGymqWhp0uV44Q/_ЛАБЫ/1%20сем/006.Торсионный%20осциллятор\n"
                                                                                                   "-общая копилка")
            if request == "лаба 8":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/008.%20Колебания%20струны/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/008\n-копилка 2\n"
                                                                                                   "https://yadi.sk/d/VGymqWhp0uV44Q/_ЛАБЫ/1%20сем/008.Колебания%20струны\n"
                                                                                                   "-общая копилка")
            if request == "лаба 9":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/009.%20Скорость%20звука/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/009\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 10":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/010.%20Генератор%20тока/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/010\n-копилка 2\n"
                                                                                                   "https://yadi.sk/d/VGymqWhp0uV44Q/_ЛАБЫ/1%20сем/010.Генератор%20тока\n"
                                                                                                   "-общая копилка")
            if request == "лаба 11":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/011.%20Аэродинамическая%20труба/\n"
                                                                                                   "-копилка стариков(11-1)\n"
                                                                                                   "https://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/011.%20Исследование%20теплопередачи%20в%20газах/\n-копилка стариков(11-2)")
            if request == "лаба 10":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/014.%20Вязкость%20жидкости/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "хз\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 14":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/014.%20Вязкость%20жидкости/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "хз\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 15":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/015.%20Поверхностное%20натяжение/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "хз\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 16":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/016.%20Теплота%20парообразования/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "хз\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 17":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/017.%20Фазовый%20переход/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "хз\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 19":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/019.%20Тепловой%20насос/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "хз\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 22":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/022.%20Адиабата/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "хз\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 23":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/023.%20Законы%20идеального%20газа/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "хз\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 24":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/024.%20Кривая%20упругости/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "хз\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 29":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/029.%20Изучение%20распределения%20случайных%20ошибок%20измерений/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/029\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 31":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/031.%20Удельный%20заряд%20электрона/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/031\n-копилка 2\n"
                                                                                                   "https://yadi.sk/d/VGymqWhp0uV44Q/_ЛАБЫ/1%20сем/031.Удельный%20заряд%20электрона\n"
                                                                                                   "-общая копилка")
            if request == "лаба 41":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/041.%20Маятник%20Катера/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/041\n-копилка 2\n"
                                                                                                   "https://yadi.sk/d/VGymqWhp0uV44Q/_ЛАБЫ/1%20сем/041.Маятник%20Катера\n"
                                                                                                   "-общая копилка")
            if request == "лаба 41":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/047.%20Скорость%20света/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/047\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 49":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/049.%20Моменты%20инерции/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/049\n-копилка 2\n"
                                                                                                   "https://yadi.sk/d/VGymqWhp0uV44Q/_ЛАБЫ/1%20сем/049.Моменты%20инерции\n"
                                                                                                   "-общая копилка")
            if request == "лаба 50":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/050.%20Проверка%20законов%20Ньютона/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/050А\n-копилка 2(50А)\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/050Б\n-копилка 2(50Б)\n"
                                                                                                   "https://yadi.sk/d/VGymqWhp0uV44Q/_ЛАБЫ/1%20сем/050.Проверка%20законов%20Ньютона\n"
                                                                                                   "-общая копилка")
            if request == "лаба 52":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/052.%20Регулировка%20токов%20и%20напряжений/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/052\n-копилка 2\n"
                                                                                                   "https://yadi.sk/d/VGymqWhp0uV44Q/_ЛАБЫ/1%20сем/052.Регулировка%20токов%20и%20напряжений\n"
                                                                                                   "-общая копилка")
            if request == "лаба 54":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/054.%20Осциллограф/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/054\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 54":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/055.%20Термопара/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "хз\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 61":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/061.%20Определение%20коэффициента%20поверхностного%20натяжения%20жидкостей/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "хз\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 91":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/090.%20Определение%20моментов%20инерции%20тел/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "хз\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "лаба 137":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = request+"\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/Лабы/1%20курс/137.%20Холодильник%20Пельтье/\n"
                                                                                                   "-копилка стариков\n"
                                                                                                   "https://disk.yandex.ru/client/disk/1%20Курс/Лабы/137\n-копилка 2\n"
                                                                                                   "хз\n"
                                                                                                   "-общая копилка")
            if request == "расписание иоф":
                ras(URLiof,xz,ret)
            if request == "расписание радиофизика":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = "Для вас впадлу писать смотрите сам")
            if request == "расписание пмф":
                ras(URL20B006,xz,ret)
            if request == "раписание иоф2020":
                ras(URLiof2020,xz,ret)
            if request == "копилка" or request == "копилки":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message = "\nhttps://cloud.mail.ru/public/E1Gt/XgKpuQDRE/ -копилка стариков\n"
                                                                                           "\nhttps://yadi.sk/d/VGymqWhp0uV44Q -копилка\n"
                                                                                           "\nhttps://yadi.sk/d/Cp1kYo1cKhb77Q -копилка №2")
            if request == "лабы":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,attachment ='wall-197891905_2',)
            #for i in razbit:
                #if i == "рома" or i == "роман" or i == "ром" or i=="рооома":
                    #vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "@psheroma(Пидорас), катриджы забери")
            if request == "лабы б04":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,attachment ='wall-197891905_3%2Fall',)

            if request == "[club197891905|@club197891905], анекдот" or request == "[club197891905|@club197891905],анекдот" or request == "рецензист, анекдот" or request == "рецензист,анекдот" or request == "рецензист анекдот":
                f=open('aneki.txt','r',encoding="utf-8")
                an=f.read().split('/')
                f.close()
                y=random.randint(0,len(an)-1)
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message =an[y],)
            if request!='' and random.random()<=0.001:
                f=open('frazi.txt','r',encoding="utf-8")
                an=f.read().split('/')
                f.close()
                y = random.randint(0, len(an)-1)
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida,message =an[y],)
