
from telebot import TeleBot
from db.service import delete_saying_by_id, get_saying_by_id
from models.user import User
from ui.enums.app_action import AppAction
from ui.enums.form_status import FormStatus
from ui.menu_options import general_menu, go_home_indicator, saying_item_delete
from utils.bot_message import bot_message


saying_to_eliminate = {}

def handle_cb_delete_saying(session:User, bot:TeleBot, chat_id:int):
    bot_message(bot, chat_id,session.user_id, FormStatus.ASK_ID_DELETE, go_home_indicator(session.user_id)) 
    session.menu_status = FormStatus.SEND_SAYING_DELETE

def handle_cb_confirm_delete(session:User, bot:TeleBot, chat_id:int):
    delete_saying_by_id(saying_to_eliminate[session.user_id].id) 
    bot_message(bot, chat_id, session.user_id, session.form_status, general_menu(session.user_id))

    session.menu_status = AppAction.INTRODUCTION
     
def handle_cb_keep_saying(session:User, bot:TeleBot, chat_id:int):
    bot_message(bot, chat_id, session.user_id, FormStatus.KEEP_SAYING, general_menu(session.user_id))
    session.menu_status = AppAction.INTRODUCTION


def handle_delete_saying (form_status:FormStatus, bot: TeleBot, chat_id: int, user_id: int, message_text:str = None) : 
    if (form_status == FormStatus.ASK_ID_DELETE) : 
        bot_message(bot, chat_id,user_id, form_status, go_home_indicator(user_id))

        return FormStatus.SEND_SAYING_DELETE

    elif (form_status == FormStatus.SEND_SAYING_DELETE):
        saying_to_eliminate[user_id] = get_saying_by_id(int(message_text))

        if (saying_to_eliminate[user_id]):
            bot_message(bot, chat_id, user_id, form_status, saying_item_delete(user_id), saying_to_eliminate[user_id])
            
        else:
             bot_message(bot, chat_id, user_id, FormStatus.NO_DATA_FOUND ,go_home_indicator(user_id))

   

