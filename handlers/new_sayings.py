

from telebot import TeleBot
from models.saying import Saying
from db.service import insert_new_saying
from models.user import User
from ui.enums.form_status import FormStatus
from ui.menu_options import general_menu, go_home_indicator
from utils.bot_message import bot_message

new_saying = {}

def handle_cb_new_saying(session: User, bot:TeleBot, chat_id:int, aditional_params:str):
    new_saying[session.user_id] = Saying("","","","")
    
    bot_message(bot, chat_id, session.user_id, FormStatus.NEW_SAYING, go_home_indicator(session.user_id))

    session.menu_status = FormStatus.WAITING_TITLE
    

def handle_mss_new_saying(message, bot:TeleBot, session:User):
    chat_id = message.chat.id
    message_text = message.text
    
    if (session.menu_status == FormStatus.WAITING_TITLE): 
        
        new_saying[session.user_id].title = message_text
        bot_message(bot, chat_id, session.user_id, session.menu_status, go_home_indicator(session.user_id))

        session.menu_status = FormStatus.WAITING_DESCRIPTION
    
    elif (session.menu_status == FormStatus.WAITING_DESCRIPTION):
        new_saying[session.user_id].description = message_text
        bot_message(bot, chat_id, session.user_id, session.menu_status, go_home_indicator(session.user_id))

        session.menu_status =  FormStatus.WAITING_AUTHOR
        
    elif (session.menu_status == FormStatus.WAITING_AUTHOR): 
        new_saying[session.user_id].author = message_text
        insert_new_saying(new_saying[session.user_id], session)
        
        bot_message(bot, chat_id, session.user_id, FormStatus.DATA_SAVED, general_menu(session.user_id))

        session.menu_status =  FormStatus.DATA_SAVED