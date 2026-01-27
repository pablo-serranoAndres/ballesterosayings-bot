from telebot import TeleBot
from models.user import User
from ui.enums.app_action import AppAction
from ui.enums.form_status import FormStatus
from ui.menu_options import available_langs, config_menu, general_menu
from utils.bot_message import bot_message
from utils.locale import switch_locale
from utils.sessions import SESSIONS


def handle_cb_switch_lang(session: User, bot: TeleBot, chat_id: int, new_lang:str):
    switch_locale(session, new_lang) 
    bot_message(bot, chat_id, session.user_id, AppAction.BACK_HOME, general_menu(session.user_id), None)
    

def handle_cb_show_config(session:User, bot:TeleBot, chat_id: int, aditional_params:str):
    session.menu_status = AppAction.CONFIG
    bot_message(bot, chat_id, session.user_id,  AppAction.CONFIG_MENU,config_menu(session.user_id), None)


def handle_cb_lang_config_button(session:User, bot:TeleBot, chat_id: int, aditional_params:str):
    session.menu_status = FormStatus.HANDLE_LANGS
    bot_message(bot, chat_id, session.user_id, SESSIONS[session.user_id].menu_status, available_langs(session.user_id))

def create_session(message):
    return User (
            user_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            lang="es",
            menu_status=FormStatus.REGISTERING_USER,
            page_limit=10)