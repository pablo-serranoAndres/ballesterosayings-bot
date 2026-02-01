import os
from telebot import TeleBot
from db.service import update_autorized
from models.user import User
from ui.enums.app_action import AppAction
from ui.menu_options import acept_reject_users, general_menu, go_home_indicator
from ui.messages.messages import build_user_auth, build_user_display, get_message
from utils.bot_message import bot_message
from utils.sessions import SESSIONS


def send_auth_to_admin(bot:TeleBot, admin_id:int, session:User):
    bot.send_message(admin_id, 
                     build_user_auth(admin_id, session), 
                     reply_markup=acept_reject_users(user_id=admin_id, new_user_id=session.user_id), 
                     parse_mode="HTML")
    
    bot.send_message(session.user_id, 
                     get_message(session.user_id,AppAction.WAITING_AUTH_USER), 
                    #  reply_markup=general_menu(user_id=user_id), 
                     parse_mode="Markdown") 


def handle_new_user(session:User, bot:TeleBot, chat_id: int, additional_params:str):
    action, target_user_id = additional_params.split("-")    

    user_session = SESSIONS.get(int(target_user_id))

    if (action == "acept"):
        user_session.autorized = True
        
        admin_feedback_str = AppAction.NEW_USER_ACEPTED
        user_feedback_str = AppAction.INTRODUCTION
        user_feedback_markup = general_menu(user_session.user_id)
        
    
    elif (action == "reject"):
        user_session.autorized = False

        admin_feedback_str = AppAction.NEW_USER_REJECTED
        user_feedback_str = AppAction.NEW_USER_REJECTED 
        user_feedback_markup = None
    
    update_autorized(user_session)
    

    # Msg to admin
    if (session.user_id == int(os.getenv("ADMIN_ID"))):
        bot_message(
            bot, 
            session.user_id, 
            session.user_id, 
            admin_feedback_str,
            general_menu(session.user_id))
    
    # Msg to user
    bot_message(bot, 
                user_session.user_id, 
                user_session.user_id, 
                user_feedback_str, 
                user_feedback_markup)


def handle_admin_users (session:User, bot:TeleBot, chat_id: int, additional_params:str):
    admin_id = session.user_id

    bot_message(bot, admin_id, admin_id, (AppAction.USER_ADMIN))

    for user_session in SESSIONS.values():
        bot.send_message(
            chat_id, 
            build_user_display(admin_id, user_session), 
            reply_markup=acept_reject_users(admin_id, user_session.user_id), 
            parse_mode="Markdown")

    bot_message(bot, admin_id, admin_id, (AppAction.HOME_PAGE),go_home_indicator(admin_id))
     