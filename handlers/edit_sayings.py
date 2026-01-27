from telebot import TeleBot
from db.service import get_saying_by_id
from models.user import User
from ui.enums.app_action import AppAction
from ui.enums.form_status import FormStatus
from ui.menu_options import go_home_indicator, saying_item_edit
from utils.bot_message import bot_message

saying_to_update = {}


def handle_cb_update_saying(session: User, bot:TeleBot, chat_id:int, additional_params:str) :
    if additional_params is  None: 
        session.menu_status = FormStatus.WAITING_ID_UPDATE
    
    else: 
        additional_params_splitted = additional_params.split("-")
        field_to_edit = additional_params_splitted[0]

        if (field_to_edit == "title"):
            session.menu_status = FormStatus.EDITING_TITLE
            
        elif (field_to_edit == "description"):
            session.menu_status = FormStatus.EDITING_DESCRIPTION

        elif (field_to_edit == "author"):
            session.menu_status = FormStatus.EDITING_AUTHOR
    

    bot_message(bot, chat_id, session.user_id, session.menu_status, go_home_indicator(session.user_id), None)


def handle_mss_update_saying(message, bot:TeleBot, session:User) :
    chat_id = message.chat.id
    message_text = message.text

    if (session.menu_status == FormStatus.WAITING_ID_UPDATE): 
        saying_to_update[session.user_id] = get_saying_by_id(int(message_text))

        if (saying_to_update[session.user_id]):
            bot_message(bot, chat_id, session.user_id, FormStatus.SEND_SAYING_UPDATE, saying_item_edit(session.user_id, saying_to_update[session.user_id].id), saying_to_update[session.user_id])
            return AppAction.EDITING_SAYING
            
        else:
             bot_message(bot, chat_id, session.user_id, FormStatus.NO_DATA_FOUND ,go_home_indicator(session.user_id))