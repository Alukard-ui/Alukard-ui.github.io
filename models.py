# *- coding: utf-8 -*

from pony.orm import Database,Required,PrimaryKey,Json
from settings import DB_CONFIG

db = Database()
db.bind(**DB_CONFIG)

class LaboratoryWork(db.Entity):
    id = PrimaryKey(str)
    oldPiggyBank = Required(str)
    newPiggyBank = Required(str)
    IOFPiggyBank = Required(str)

class UserState(db.Entity):
    user_id = Required(str,unique=True)
    scenario_name = Required(str)
    step_name = Required(str)
    context = Required(Json)

db.generate_mapping(create_tables=True)
