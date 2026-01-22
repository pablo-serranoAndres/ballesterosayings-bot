from telebot import TeleBot
from ui.enums.app_action import AppAction
from ui.menu_options import available_langs
from utils.bot_message import bot_message


def handle_configuration(bot:TeleBot, chat_id: int, user_id: int, action: AppAction):

    bot_message(bot, chat_id, user_id, action, available_langs(user_id))
    available_langs(user_id)
    return "holi"

