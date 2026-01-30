from telebot import TeleBot
from db.service import update_autorized
from models.user import User
from ui.enums.app_action import AppAction
from ui.menu_options import acept_reject_new_users, general_menu
from ui.messages.messages import build_user_auth, get_message
from utils.bot_message import bot_message
from utils.sessions import SESSIONS


def send_auth_to_admin(bot:TeleBot, admin_id:int, session:User):
    bot.send_message(admin_id, 
                     build_user_auth(admin_id, session), 
                     reply_markup=acept_reject_new_users(user_id=admin_id, new_user_id=session.user_id), 
                     parse_mode="HTML")
    
    bot.send_message(session.user_id, 
                     get_message(session.user_id,AppAction.WAITING_AUTH_USER), 
                    #  reply_markup=general_menu(user_id=user_id), 
                     parse_mode="Markdown") 


def handle_acept_new_user(session:User, bot:TeleBot, chat_id: int, id_new_user:str):

    new_user_session = SESSIONS.get(int(id_new_user))
    new_user_session.autorized = True
    new_user_session.menu_status = AppAction.INTRODUCTION

    update_autorized(new_user_session)

    bot_message(bot, chat_id, session.user_id, AppAction.NEW_USER_ACEPTED)
    bot_message(bot, new_user_session.user_id, new_user_session.user_id, new_user_session.menu_status, general_menu(new_user_session.user_id))


def handle_reject_new_user(session:User, bot:TeleBot, chat_id: int, id_new_user:str):
    new_user_session = SESSIONS.get(int(id_new_user))
    new_user_session.autorized = False

    update_autorized(new_user_session)

    bot_message(bot, chat_id, session.user_id, AppAction.NEW_USER_REJECTED)
    bot_message(bot, new_user_session.user_id, new_user_session.user_id, AppAction.NEW_USER_REJECTED)