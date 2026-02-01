import os
from typing import List
from telebot import TeleBot
from db.service import get_all_users, update_autorized
from models.user import User
from ui.enums.app_action import AppAction
from ui.enums.help_feedback import HelpFeedback
from ui.menu_options import acept_reject_users, general_menu, go_home_indicator, next_previous_indicators
from ui.messages.messages import build_user_auth, build_user_display, get_help_message, get_message
from utils.bot_message import bot_message
from utils.sessions import SESSIONS


def get_formatted_users():
    users_dto = get_all_users()
    users : list[User] = []

    for user_dto in users_dto :
        new_user = (User ( 
            user_id=user_dto[1],
            first_name=user_dto[2],
            last_name="",
            menu_status=user_dto[3],
            offset=user_dto[4],
            page_limit=user_dto[5],
            lang=user_dto[6],
        ))
        new_user.autorized = True if user_dto[7] == 1 else False
        users.append(new_user)

    return users


def show_users_paginated(bot:TeleBot, admin_id: int):
    bot_message(bot, admin_id, admin_id, (AppAction.USER_ADMIN))

    for user in get_formatted_users():
        bot.send_message(
            admin_id, 
            build_user_display(admin_id, user), 
            reply_markup=acept_reject_users(admin_id, user.user_id), 
            parse_mode="Markdown")
    
    bot.send_message(
            admin_id, 
            get_help_message(admin_id, HelpFeedback.USERS_PAGINATION_OPTIONS), 
            reply_markup=next_previous_indicators(admin_id), 
            parse_mode="Markdown")

def send_auth_to_admin(bot:TeleBot, admin_id:int, session:User):
    bot.send_message(admin_id, 
                     build_user_auth(admin_id, session), 
                     reply_markup=acept_reject_users(user_id=admin_id, new_user_id=session.user_id), 
                     parse_mode="HTML")
    
    bot.send_message(session.user_id, 
                     get_message(session.user_id,AppAction.WAITING_AUTH_USER), 
                    #  reply_markup=general_menu(user_id=user_id), 
                     parse_mode="Markdown") 


def handle_user(session:User, bot:TeleBot, chat_id: int, additional_params:str):
    action, target_user_id = additional_params.split("-")    

    print (additional_params)
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
        if (session.menu_status == AppAction.USER_ADMIN) : 
            show_users_paginated(bot, session.user_id)
        else: 
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

    session.menu_status = AppAction.USER_ADMIN
    session.offset = 0
    
    show_users_paginated(bot, admin_id)
    
    # bot_message(bot, admin_id, admin_id, (AppAction.HOME_PAGE),go_home_indicator(admin_id))
     