from telebot import TeleBot
from db.service import get_saying_by_id
from ui.enums.app_action import AppAction
from ui.enums.form_status import FormStatus
from ui.menu_options import go_home_indicator, saying_item_edit
from utils.bot_message import bot_message

saying_to_update = {}

def handle_update_saying(status:FormStatus, bot:TeleBot, chat_id:int, user_id:int,message_text:str = None) :
    if (status == FormStatus.ASK_ID_UPDATE):
        bot_message(bot, chat_id, user_id, FormStatus.ASK_ID_UPDATE,None, None)
        return FormStatus.WAITING_ID_UPDATE
    
    elif (status == FormStatus.WAITING_ID_UPDATE): 
        saying_to_update[user_id] = get_saying_by_id(int(message_text))

        if (saying_to_update[user_id]):
            bot_message(bot, chat_id, user_id, FormStatus.SEND_SAYING_UPDATE, saying_item_edit(user_id), saying_to_update[user_id])
            return AppAction.EDITING_SAYING
            
        else:
             bot_message(bot, chat_id, user_id, FormStatus.NO_DATA_FOUND ,go_home_indicator(user_id))