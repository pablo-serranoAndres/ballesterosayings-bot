

from telebot import TeleBot
from models.saying import Saying
from db.service import insert_new_saying
from ui.enums.form_status import FormStatus
from ui.menu_options import general_menu, go_home_indicator
from utils.bot_message import bot_message

new_saying = {}

def handle_new_saying(form_status:FormStatus, user_id:int, bot:TeleBot, chat_id:int, message_text:str = None):
    
    if (form_status == FormStatus.NEW_SAYING): 
        new_saying[user_id] = Saying("","","","")
        bot_message(bot, chat_id, user_id, form_status, go_home_indicator(user_id))
        
        return FormStatus.WAITING_TITLE
    
    elif (form_status == FormStatus.WAITING_TITLE): 
        
        new_saying[user_id].title = message_text
        bot_message(bot, chat_id, user_id, form_status, go_home_indicator(user_id))

        return FormStatus.WAITING_DESCRIPTION
    
    elif (form_status == FormStatus.WAITING_DESCRIPTION):
        new_saying[user_id].description = message_text
        bot_message(bot, chat_id, user_id, form_status, go_home_indicator(user_id))

        return FormStatus.WAITING_AUTHOR
        
    elif (form_status == FormStatus.WAITING_AUTHOR): 
        new_saying[user_id].author = message_text
        insert_new_saying(new_saying[user_id], user_id)
        
        bot_message(bot, chat_id, user_id, FormStatus.DATA_SAVED, general_menu(user_id))

        return FormStatus.DATA_SAVED