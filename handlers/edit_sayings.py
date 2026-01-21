from telebot import TeleBot
from ui.enums.app_action import AppAction
from utils import bot_message


def handle_edit_saying(app_action:AppAction, bot: TeleBot, chat_id: int) :
    if (app_action == AppAction.SEND_SAYING_EDIT) :
        bot_message(bot, chat_id, app_action, None, None)
        print ("handle_edit_saying")