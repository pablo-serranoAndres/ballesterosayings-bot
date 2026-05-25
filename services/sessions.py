

from config import ADMIN_ID
from db.service import get_user_by_id, insert_new_user
from enums.app_action import AppAction
from models.user import User
from ui.keyboard_factory import admin_general_menu, general_menu
from utils.bot_message import bot_message


SESSIONS: dict[int, User] = {}

def load_session_fromRAM (user_id: int):
    return SESSIONS.get(user_id)

def load_session_fromDB (user_id: int):
    user = get_user_by_id(user_id)
    if (user is not None):
        return user

def create_session (message):
    new_user =  User (
            user_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            lang="es",
            menu_status=AppAction.REGISTERING_USER,
            page_limit=10)
    
    SESSIONS[message.from_user.id] = new_user
    insert_new_user(new_user)

    return new_user

def check_session_access (session: User, chat_id: int):
    print ("check_session_access")

    if (session.user_id == ADMIN_ID):
        bot_message(session)
        # bot_message(chat_id, 
        #             session.user_id, 
        #             AppAction.MAIN_MENU, 
        #             admin_general_menu(session.user_id))
        
    elif (session.autorizated):
        session.menu_status = AppAction.MAIN_MENU

        bot_message(chat_id, 
                    session.user_id, 
                    session.menu_status, 
                    general_menu(session.user_id))
    else : 
        print("TODO")

