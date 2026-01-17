
from enum import Enum
from telebot import TeleBot
from models.saying import Saying
from db.service import insert_new_saying
from ui.menu_options import go_home_indicator
from utils.locale import LOCALE

new_saying = {}

class FormMessages(Enum):
    NEW_TITLE = "ask_new_title"
    NEW_DESCRIPTION = "ask_new_description"
    NEW_AUTHOR = "ask_new_author"
    DATA_SAVED = "saved_data"

def send_message(bot, form_message:FormMessages, chat_id):

    feedback_map = {
        FormMessages.NEW_TITLE: LOCALE["forms"]["new_saying"]["new_title"],
        FormMessages.NEW_DESCRIPTION: LOCALE["forms"]["new_saying"]["new_description"],
        FormMessages.NEW_AUTHOR: LOCALE["forms"]["new_saying"]["new_author"],
        FormMessages.DATA_SAVED: LOCALE["forms"]["new_saying"]["save_saying"],
    }

    feedback_message = feedback_map.get(form_message, "Desconocido")
    
    bot.send_message(
        chat_id,
        feedback_message,
        reply_markup=go_home_indicator(),
        parse_mode="Markdown")

def ask_new_title(user_id, bot, chat_id):
    new_saying[user_id] = Saying("","","","")
    send_message(bot, FormMessages.NEW_TITLE, chat_id)

    return "waiting_new_saying_title"

def handle_new_title(user_id, bot, chat_id, message):
    new_saying[user_id].title = message
    send_message(bot,FormMessages.NEW_DESCRIPTION, chat_id)

    return "waiting_new_saying_description"

def handle_new_description(user_id, bot, chat_id, message):
    new_saying[user_id].description = message
    send_message(bot,FormMessages.NEW_AUTHOR, chat_id)

    return "waiting_new_saying_author"

def handle_new_author(user_id, bot, chat_id, message):
    new_saying[user_id].author = message
    insert_new_saying(new_saying[user_id], user_id)
    send_message(bot, FormMessages.DATA_SAVED, chat_id)

    return "new_saying_terminated"

def handle_new_saying(status:str, user_id:int, bot:TeleBot, chat_id:int, message:str):
    if (status == "waiting_new_saying_title"): 
        return handle_new_title(user_id, bot, chat_id, message)

    elif (status == "waiting_new_saying_description"): 
        return handle_new_description(user_id, bot, chat_id, message)

    elif (status == "waiting_new_saying_author"): 
        return handle_new_author(user_id, bot, chat_id, message)
    
    elif (status == "ask_title"): 
        return ask_new_title(user_id, bot, chat_id)
