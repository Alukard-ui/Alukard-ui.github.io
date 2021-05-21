#*- coding:utf-8 -*

log_config ={
    "version":1,
    "formatters":{
        "default":{
            "format":"[%(asctime)s %(name)s %(levelname)s] %(message)s"
        },
    },
    "handlers":{
        "file_handler":{
            "class":"logging.FileHandler",
            "formatter":"default",
            "filename":"bot.log",
            "encoding":"utf-8"
        },
    },
    "loggers":{
        "bot":{
            "handlers":["file_handler"],
            "level":"INFO"
        }
    }
}