from telebot import TeleBot
from db.service import count_sayings, count_users
from handlers.admin import show_users_paginated
from handlers.select_sayings import show_sayings_paginated
from models.user import User
from ui.enums.app_action import AppAction
from ui.menu_options import general_menu
from utils.bot_message import bot_message


def handle_cb_go_home(session:User, bot:TeleBot, chat_id:int, aditional_params:str):
    bot_message(bot, chat_id, session.user_id, AppAction.BACK_HOME, general_menu(session.user_id), None)
    session.menu_status = AppAction.INTRODUCTION


def handle_cb_go_next(session:User, bot:TeleBot, chat_id:int, aditional_params:str):
    max_count = count_sayings() if AppAction.WATCHING_SAYINGS else  count_users()

    if (max_count < session.offset + 10):
        session.offset = 0
    else :
        session.offset = session.offset + 10
    
    if (session.menu_status == AppAction.WATCHING_SAYINGS):
        show_sayings_paginated(bot, chat_id, session)
        
    elif (session.menu_status == AppAction.USER_ADMIN):
        show_users_paginated(bot, session.user_id)

def handle_cb_go_previous(session:User, bot:TeleBot, chat_id:int, aditional_params:str):
    
    max_count = count_sayings() if AppAction.WATCHING_SAYINGS else count_users()

    if (session.offset - 10 < 0):
        session.offset = (max_count // 10) * 10
    else:
        session.offset -= 10


    if (session.menu_status == AppAction.WATCHING_SAYINGS ):
        show_sayings_paginated(bot, chat_id, session)

    elif (session.menu_status == AppAction.USER_ADMIN):
        show_users_paginated(bot, session.user_id)