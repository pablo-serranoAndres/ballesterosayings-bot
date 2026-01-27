from telebot import TeleBot
from db.service import count_sayings
from handlers.select_sayings import show_sayings_paginated
from models.user import User
from ui.enums.app_action import AppAction
from ui.menu_options import general_menu
from utils.bot_message import bot_message
from utils.sessions import SESSIONS


def handle_cb_go_home(session:User, bot:TeleBot, chat_id:int):
    bot_message(bot, chat_id, session.user_id, AppAction.BACK_HOME, general_menu(session.user_id), None)
    SESSIONS[session.user_id].menu_status = AppAction.INTRODUCTION


def handle_cb_go_next(session:User, bot:TeleBot, chat_id:int):
    if (count_sayings() < session.offset + 10):
        SESSIONS[session.user_id].offset = 0
    
    else :
        SESSIONS[session.user_id].offset = SESSIONS[session.user_id].offset + 10

    show_sayings_paginated(bot, chat_id, SESSIONS[session.user_id])
    
def handle_cb_go_previous(session:User, bot:TeleBot, chat_id:int):
    total = count_sayings()

    if (SESSIONS[session.user_id].offset - 10 < 0):
        SESSIONS[session.user_id].offset = (total // 10) * 10
    else:
        SESSIONS[session.user_id].offset -= 10

    show_sayings_paginated(bot, chat_id, SESSIONS[session.user_id])