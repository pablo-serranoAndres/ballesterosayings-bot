from telebot import TeleBot
from db.service import get_all_sayings_by_user, get_saying_by_id, update_saying_by_id
from models.user import User
from enums.app_action import AppAction
from enums.form_status import AppAction
from ui.keyboard_factory import go_home_indicator, next_previous_indicators, saying_item_edit, sayings_to_edit
from utils.bot_message import bot_message

saying_to_update = {}

def handle_cb_edit_opt(session: User, bot:TeleBot, chat_id:int, additional_params:str): 
    clicked_opt = additional_params.split("-")[0]

    if (clicked_opt == "title"):
        session.menu_status = AppAction.EDITING_TITLE

    elif (clicked_opt == "description"):
        session.menu_status = AppAction.EDITING_DESCRIPTION

    elif (clicked_opt == "author"):
        session.menu_status = AppAction.EDITING_AUTHOR

def handle_cb_show_editing_opts(session: User, bot:TeleBot, chat_id:int, additional_params:str):
    
    saying_to_update[session.user_id] = get_saying_by_id(additional_params)
    
    bot_message(bot, 
                chat_id, 
                session.user_id, 
                session.menu_status, 
                saying_item_edit(session.user_id, additional_params), 
                saying_to_update[session.user_id])

def handle_cb_save_update_saying(session: User, bot:TeleBot, chat_id:int, additional_params:str):
    update_saying_by_id(saying_to_update[session.user_id], session)

def handle_cb_edit_sayings(session: User, bot:TeleBot, chat_id:int, additional_params:str):
    bot_message(bot, 
                chat_id, 
                session.user_id, 
                AppAction.EDITING_SAYINGS, 
                sayings_to_edit(session.user_id, get_all_sayings_by_user(session)))
    
    

def handle_mss_update_saying(message, bot:TeleBot, session:User) :
    chat_id = message.chat.id
    message_text = message.text

    if (session.menu_status == AppAction.WAITING_ID_UPDATE): 
        saying_to_update[session.user_id] = get_saying_by_id(int(message_text))
    
    if(session.menu_status == AppAction.EDITING_TITLE):
        saying_to_update[session.user_id].title = message_text

    if(session.menu_status == AppAction.EDITING_DESCRIPTION):
        saying_to_update[session.user_id].description = message_text
    
    if(session.menu_status == AppAction.EDITING_AUTHOR):
        saying_to_update[session.user_id].author = message_text

    session.menu_status = AppAction.EDITING_SAYINGS
    
    bot_message(bot, 
                chat_id, 
                session.user_id, 
                AppAction.SEND_SAYING_UPDATE, 
                markup= saying_item_edit(session.user_id, saying_to_update[session.user_id].id), 
                saying= saying_to_update[session.user_id])

             