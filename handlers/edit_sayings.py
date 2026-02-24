from telebot import TeleBot
from db.service import get_all_sayings_by_user, get_saying_by_id, update_saying_by_id
from models.user import User
from ui.enums.app_action import AppAction
from ui.enums.form_status import FormStatus
from ui.menu_options import go_home_indicator, saying_item_edit, sayings_to_edit
from utils.bot_message import bot_message

saying_to_update = {}


def handle_cb_edit_saying(session: User, bot:TeleBot, chat_id:int, additional_params:str):
    session.menu_status = FormStatus.WAITING_ID_UPDATE
    
    bot_message(bot, 
                chat_id, 
                session.user_id, 
                session.menu_status, 
                go_home_indicator(session.user_id))


def handle_cb_save_update_saying(session: User, bot:TeleBot, chat_id:int, additional_params:str):
    update_saying_by_id(saying_to_update[session.user_id], session)

def handle_cb_update_saying(session: User, bot:TeleBot, chat_id:int, additional_params:str):
    bot_message(bot, 
                chat_id, 
                session.user_id, 
                AppAction.EDITING_SAYING, 
                sayings_to_edit(session.user_id, get_all_sayings_by_user(session)))


# def handle_cb_update_saying(session: User, bot:TeleBot, chat_id:int, additional_params:str) :
#     if not additional_params: 
#         session.menu_status = FormStatus.WAITING_ID_UPDATE
#         bot_message(bot, 
#                     chat_id, 
#                     session.user_id, 
#                     session.menu_status, 
#                     go_home_indicator(session.user_id))
    
#     else:
#         edit_field, edit_id = additional_params.split("-")
#         current_saying = saying_to_update.get(session.user_id)

#         if (not current_saying or current_saying.id != edit_id):
#             session.menu_status = AppAction.INTRODUCTION
#             bot_message(bot, 
#                         chat_id, 
#                         session.user_id, 
#                         AppAction.APP_ERROR, 
#                         general_menu(session.user_id))
#             return
        
#         else: 
#             markup = go_home_indicator(session.user_id)

#             if (edit_field == "title"):
#                 session.menu_status = FormStatus.EDITING_TITLE
                
#             elif (edit_field == "description"):
#                 session.menu_status = FormStatus.EDITING_DESCRIPTION

#             elif (edit_field == "author"):
#                 session.menu_status = FormStatus.EDITING_AUTHOR
    
#         bot_message(bot, chat_id, session.user_id, session.menu_status, markup, None)


def handle_mss_update_saying(message, bot:TeleBot, session:User) :
    chat_id = message.chat.id
    message_text = message.text

    if (session.menu_status == FormStatus.WAITING_ID_UPDATE): 
        saying_to_update[session.user_id] = get_saying_by_id(int(message_text))
    
    if(session.menu_status == FormStatus.EDITING_TITLE):
        saying_to_update[session.user_id].title = message_text

    if(session.menu_status == FormStatus.EDITING_DESCRIPTION):
        saying_to_update[session.user_id].description = message_text
    
    if(session.menu_status == FormStatus.EDITING_AUTHOR):
        saying_to_update[session.user_id].author = message_text

    session.menu_status = AppAction.EDITING_SAYING
    
    bot_message(bot, 
                chat_id, 
                session.user_id, 
                FormStatus.SEND_SAYING_UPDATE, 
                markup= saying_item_edit(session.user_id, saying_to_update[session.user_id].id), 
                saying= saying_to_update[session.user_id])

             