import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

vk = vk_api.VkApi(token="919e919e3815b66463acace0ec808f8e88d010e3e2863477fb93d1542a70cdc48245ee3622e9318f7320c")
longpoll = VkBotLongPoll(vk, '197891905')
vk = vk.get_api()

print("Бот запущен")

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            request = event.object.message['text'].lower()
            peer_ida = event.object.message['peer_id']
            reply = event.object.message['date']
            linka = event.object.message['attachments']
            razbit = request.replace(',','').replace('?',' ').replace('!',' ').replace('.',' ').split(' ')
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
                if i == "ансис":
                    vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Забудь нахуй")
                if i == "ансису":
                    vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Забудь нахуй")
                if i == "ансисом":
                    vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Забудь нахуй")
                if i == "ансиса":
                    vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Забудь нахуй")
                if i == "ansys":
                    vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Забудь нахуй")
            if request == "что делать с матаном?":
                vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Иди ботай")