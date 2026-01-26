from telebot import TeleBot
from db.service import insert_new_user
from models.user import User
from ui.enums.app_action import AppAction
from ui.enums.form_status import FormStatus
from ui.menu_options import available_langs
from utils.bot_message import bot_message


def handle_configuration(bot:TeleBot, chat_id: int, user_id: int, action: AppAction):

    bot_message(bot, chat_id, user_id, action, available_langs(user_id))
    return FormStatus.HANDLE_LANGS


def create_session(message):
    return User (
            user_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            lang="es",
            menu_status=FormStatus.REGISTERING_USER,
            page_limit=10)