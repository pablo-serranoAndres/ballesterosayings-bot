




import os
from dotenv import load_dotenv
import telebot
from db.config import check_versions_db
from db.service import insert_new_user
from handlers.admin import handle_user, send_auth_to_admin
from handlers.configurate_bot import create_session
from handlers.dispatch import dispatch_callback, dispatch_message
from ui.enums.app_action import AppAction
from ui.menu_options import general_menu
from ui.messages.messages import get_message
from utils.locale import open_locale
from utils.sessions import SESSIONS


load_dotenv()
check_versions_db()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def initialize_bot(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    session = SESSIONS.get(user_id) 
    
    if not session:
        SESSIONS[user_id] = create_session(message)
        session = SESSIONS[user_id]
    
    open_locale(user_id)

    if (session.autorized == False):
        handle_user(session, bot, chat_id, f'reject-{user_id}')      
        return

    if (session.user_id == ADMIN_ID):
        session.autorized = True
    else: 
        send_auth_to_admin(bot, ADMIN_ID, session)
    
    insert_new_user(session)

    if (session.autorized == True): 
        bot.send_message(chat_id, get_message(user_id,AppAction.INTRODUCTION) , reply_markup=general_menu(user_id=user_id), parse_mode="Markdown") 
    
    elif (session.autorized == False) :
        handle_user(session, bot, chat_id, f'reject-{user_id}')


@bot.message_handler(content_types=["text"])
def onText(message):
    session = SESSIONS.get(message.from_user.id)

    if not session: 
        session = create_session(message)
        SESSIONS[message.from_user.id] = session

    dispatch_message(message, bot, session)


@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    user_id = call.from_user.id

    session = SESSIONS.get(user_id)

    if not session: 
        session = create_session(call.message)
        SESSIONS[user_id] = session
    
    if session.autorized == True:
        dispatch_callback(call, bot, session)
    else: 
        handle_user(session, bot, call.message.chat.id, f'reject-{user_id}')

if __name__ == "__main__":
    bot.infinity_polling()
