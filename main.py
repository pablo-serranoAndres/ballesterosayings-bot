


from config import bot
from db.config import check_versions_db
from handlers.dispatch import dispatch_callback
from services.sessions import check_session_access, create_session, load_session_fromDB, load_session_fromRAM
from ui.keyboard_factory import *
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

    check_session_access(session)


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
    dispatch_callback(call, bot, session)

if __name__ == "__main__":
    bot.infinity_polling()
