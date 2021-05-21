group_id = '197891905'
token = "919e919e3815b66463acace0ec808f8e88d010e3e2863477fb93d1542a70cdc48245ee3622e9318f7320c"

INTENTS = [
    {
        'name': 'Кричалка',
        'tokens': ("физфак", "физфак"),
        'scenario': None,
        'answer': 'Чемпион'
    },
    {
        'name': 'laboratoryWork',
        'tokens': ("лабораторная работа", "лаба"),
        'scenario': 'laboratoryWork',
        'answer': None
    },
{
        'name': 'PiggyBank',
        'tokens': ("копилка", "копилки"),
        'scenario': None,
        'answer': 'https://cloud.mail.ru/public/E1Gt/XgKpuQDRE/ - копилка стариков\n'
                  'https://disk.yandex.ru/d/VGymqWhp0uV44Q - копилка\n'
                  'https://disk.yandex.ru/d/Cp1kYo1cKhb77Q - копилка №2'
    },
    {
        'name':'Help',
        'tokens':('рецензист','рецензист'),
        'scenario':None,
        'answer':'Руководсто по ебле рецензиста:\n'
                 '1.Для вызова лаб достаточно ввсети №[курс][номер лабы], для бесед и оправить сообщение с текстом'
                 '"лаба" или "лабораторная работа"'
    }
]

SCENARIOS = {
    'laboratoryWork': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Введи свой курс',
                'failure_text': 'Курс не обнаружен',
                'handler': 'handler_class',
                'next_step': 'step2'
            },
            'step2': {
                'text': 'Введи номер лабораторной работы',
                'failure_text': 'Лабораторная работа не обнаружена',
                'handler': 'handler_numberLab',
                'next_step': 'step3'
            },
            'step3': {
                'text': 'Вам нужна лабороторная работа №{numberLab} для {class} курса, {first_name}?',
                'failure_text': 'Ответь да',
                'handler': 'handler_link',
                'next_step': 'step4'
            },
            'step4': {
                'text': 'Вот ссылки на лабораторную работу №{numberLab} для {class} курса\n'
                        '{oldPiggyBank} - Копилка стариков\n'
                        '{newPiggyBank} - копилка\n'
                        '{IOFPiggyBank} - копилка №2',
                'failure_text': None,
                'handler': None,
                'next_step': None
            }
        }
    }
}

DEFAULT_ANSWER = 'Я хз'

DB_CONFIG = dict(
    provider='sqlite',
    filename='Reviewer.db'
)
