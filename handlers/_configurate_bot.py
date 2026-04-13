from telebot import TeleBot
from db.service import insert_new_user
from models.user import User
from enums.app_action import AppAction
from enums.form_status import AppAction
from services.sessions import SESSIONS
from ui.keyboard_factory import available_langs, config_menu, general_menu
from utils.bot_message import bot_message
from utils.locale import switch_locale


def handle_cb_switch_lang(session: User, bot: TeleBot, chat_id: int, new_lang:str):
    switch_locale(session, new_lang) 
    bot_message(bot, chat_id, session.user_id, AppAction.BACK_HOME, general_menu(session.user_id), None)
    

def handle_cb_show_config(session:User, bot:TeleBot, chat_id: int, aditional_params:str):
    session.menu_status = AppAction.CONFIG
    bot_message(bot, chat_id, session.user_id,  AppAction.CONFIG_MENU,config_menu(session.user_id), None)


def handle_cb_lang_config_button(session:User, bot:TeleBot, chat_id: int, aditional_params:str):
    session.menu_status = AppAction.HANDLE_LANGS
    bot_message(bot, chat_id, session.user_id, SESSIONS[session.user_id].menu_status, available_langs(session.user_id))

