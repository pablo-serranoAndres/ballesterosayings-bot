
from telebot import TeleBot
from db.service import delete_saying_by_id, get_saying_by_id
from models.user import User
from ui.enums.app_action import AppAction
from ui.enums.form_status import FormStatus
from ui.menu_options import general_menu, go_home_indicator, saying_item_delete
from utils.bot_message import bot_message


saying_to_eliminate = {}

def handle_cb_delete_saying(session:User, bot:TeleBot, chat_id:int, aditional_params:str):
    bot_message(bot, chat_id,session.user_id, FormStatus.ASK_ID_DELETE, go_home_indicator(session.user_id)) 
    session.menu_status = FormStatus.SEND_SAYING_DELETE

def handle_cb_confirm_delete(session:User, bot:TeleBot, chat_id:int, aditional_params:str):
    delete_saying_by_id(saying_to_eliminate[session.user_id].id) 
    bot_message(bot, chat_id, session.user_id, session.menu_status, general_menu(session.user_id))

    session.menu_status = AppAction.INTRODUCTION
     
def handle_cb_keep_saying(session:User, bot:TeleBot, chat_id:int, aditional_params:str):
    bot_message(bot, chat_id, session.user_id, FormStatus.KEEP_SAYING, general_menu(session.user_id))
    session.menu_status = AppAction.INTRODUCTION


def handle_mss_delete_saying (message, bot:TeleBot, session:User) : 
    chat_id = message.chat.id
    message_text = message.text
    

    if (session.menu_status == FormStatus.ASK_ID_DELETE) : 
        bot_message(bot, chat_id,session.user_id, session.menu_status, go_home_indicator(session.user_id))

        return FormStatus.SEND_SAYING_DELETE

    elif (session.menu_status == FormStatus.SEND_SAYING_DELETE):
        saying_to_eliminate[session.user_id] = get_saying_by_id(int(message_text))

        if (saying_to_eliminate[session.user_id]):
            bot_message(bot, chat_id, session.user_id, session.menu_status, saying_item_delete(session.user_id), saying_to_eliminate[session.user_id])
            
        else:
             bot_message(bot, chat_id, session.user_id, FormStatus.NO_DATA_FOUND ,go_home_indicator(session.user_id))

   

