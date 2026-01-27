from typing import List
from db.repository import handle_db
from models.saying import Saying
from models.user import User
from ui.enums.db_action import DBAction


def count_sayings():
    count_sayings_DTO = handle_db("count_sayings")
    rows = count_sayings_DTO.fetchone()

    return rows[0] if rows else 0

def format_sayings(sayings_DTO):
    sayings_formatted: List[Saying] = []

    for saying_DTO in sayings_DTO: 
        sayings_formatted.append(
            Saying(saying_DTO[0], saying_DTO[1], saying_DTO[2], saying_DTO[3]))
    
    return sayings_formatted

def get_all_sayings(session:User):
    sayings_DTO = handle_db(action=DBAction.SELECT_SAYINGS, session=session,)
    
    return format_sayings(sayings_DTO)

def insert_new_saying(saying: Saying, user_id: int):
    handle_db(action="insert_new_saying",saying=saying, user_id=user_id)

def get_saying_by_id(saying_id:int):
    saying_DTO = handle_db("select_by_id", saying_id=saying_id)


    if (saying_DTO) :
        saying_selected = Saying (
            id= saying_DTO[0],
            title= saying_DTO[1],
            description= saying_DTO[2],
            author= saying_DTO[3],
            )
        return saying_selected
    else :
        return None
    
def delete_saying_by_id (saying_id): 
    handle_db(action="delete_saying",saying_id=saying_id)


# def get_lang_config (user_id: int): 
#     config_DAW = handle_db(
#         action=DBAction.GET_LANG_CONFIG,
#         user_id=user_id)
    
#     lang_config = config_DAW.fetchone()[0]

    
#     return lang_config

# def insert_lang (user_id: int, new_lang:str):
#     handle_db(action=DBAction.INSERT_NEW_LANG, user_id=user_id, new_lang=new_lang)

def update_lang (session: User):
    handle_db(action=DBAction.UPDATE_LANG_CONFIG, session=session,)

def insert_new_user (session: User):
    handle_db(action=DBAction.INSERT_USER, session=session, )

def get_user_by_id (session: User) -> User:
    user = handle_db(action=DBAction.GET_USER_BY_ID, user_id=session.user_id)
    return user




