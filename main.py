from config import ADMIN_ID, bot
from db.config import check_versions_db
from enums.app_action import AppAction
from handlers.dispatch import dispatch_callback
from services.sessions import SESSIONS, create_session, load_session_fromDB, load_session_fromRAM
from ui.keyboard_factory import admin_general_menu, general_menu
from utils.bot_message import bot_message
from utils.locale import open_locale


check_versions_db()

@bot.message_handler(commands=['start'])
def initialize_bot(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    SESSIONS[user_id] = (
        load_session_fromRAM(user_id) or 
        load_session_fromDB(user_id) or 
        create_session(message)
    )

    session = SESSIONS[user_id] 
    
    open_locale(user_id)

    bot_message(user_id, AppAction.MAIN_MENU)
   



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
        handle_cb_user(session, bot, call.message.chat.id, f'reject-{user_id}')

if __name__ == "__main__":
    bot.infinity_polling()
