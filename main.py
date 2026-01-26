import os
from dotenv import load_dotenv
import telebot
from db.config import check_versions_db
from db.service import count_sayings, insert_new_user
from handlers.configurate_bot import create_session, handle_configuration
from handlers.delete_sayings import handle_delete_saying
from handlers.edit_sayings import handle_update_saying
from handlers.new_sayings import handle_new_saying
from handlers.select_sayings import show_sayings_paginated
from ui.enums.app_action import AppAction
from ui.enums.form_status import FormStatus
from ui.menu_options import config_menu, general_menu
from ui.messages.messages import get_message
from utils.bot_message import bot_message
from utils.locale import open_locale, switch_locale
from utils.sessions import SESSIONS


load_dotenv()
check_versions_db()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

menu_status = {}
offset = {}


@bot.message_handler(commands=['start'])
def initialize_bot(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if (SESSIONS.get(user_id) is None) :
        SESSIONS[user_id] = create_session(message)
        insert_new_user(SESSIONS[user_id])

    open_locale(user_id)
    bot.send_message(message.chat.id, get_message(user_id,AppAction.INTRODUCTION), reply_markup=general_menu(user_id=user_id), parse_mode="Markdown") 

# Manejador de respuestas del usuario
@bot.message_handler(content_types=["text"])
def onText(message):
    session = SESSIONS[message.from_user.id]
    chat_id = message.chat.id
    message_text = message.text

    if session.menu_status in (
        
        FormStatus.WAITING_TITLE,
        FormStatus.WAITING_DESCRIPTION,
        FormStatus.WAITING_AUTHOR,
    ):
        session.menu_status = handle_new_saying(session.menu_status, session.user_id, bot, chat_id, message_text)

    if (session.menu_status == FormStatus.SEND_SAYING_DELETE):
        handle_delete_saying(session.menu_status, bot, chat_id, session.user_id, message_text)
    
    if (session.menu_status == FormStatus.WAITING_ID_UPDATE) :
        session.menu_status = handle_update_saying(FormStatus.WAITING_ID_UPDATE, bot, chat_id, session.user_id, message_text)
        


# Manejador del menú
@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    global menu_status
    global offset
    session = SESSIONS[call.from_user.id]
    chat_id = call.message.chat.id
    # Menú general
    if call.data == AppAction.INSERT_NEW_SAYING.value:
        menu_status[session.user_id] = handle_new_saying(FormStatus.NEW_SAYING, session.user_id, bot, chat_id, None)

    elif call.data == AppAction.UPDATE_SAYING.value: 
        menu_status[session.user_id] = handle_update_saying(FormStatus.ASK_ID_UPDATE, bot, chat_id, session.user_id)
    
    elif call.data == AppAction.WATCH_ALL_SAYINGS.value:
        session.offset = 0
        session.menu_status = AppAction.WATCHING_SAYINGS.value


        show_sayings_paginated(bot, chat_id, session)
    
    elif call.data == AppAction.CONFIG.value: 
        bot_message(bot, chat_id, session.user_id,  AppAction.CONFIG_MENU,config_menu(session.user_id), None)

    elif call.data == AppAction.LANG_CONFIG_BUTTON.value:
        session.menu_status = handle_configuration(bot, chat_id, session.user_id, AppAction.LANG_OPTIONS)
        # bot.send_message(chat_id, "Lenguajes disponibles: ", reply_markup=show_langs_menu(), parse_mode="Markdown" )
    
    elif call.data.startswith("btn_switch_lang_to"):
        order = len (call.data.split("_")) - 1
        new_lang = call.data.split("_")[order]

        switch_locale(session.user_id, new_lang) 
        bot_message(bot, chat_id, session.user_id, AppAction.BACK_HOME, general_menu(session.user_id), None)

    # Lógica de 'Eliminar dichos'
    elif call.data == AppAction.DELETE_SAYING.value: 
        session.menu_status = handle_delete_saying(FormStatus.ASK_ID_DELETE, bot, chat_id, session.user_id)
    
    elif call.data == AppAction.CONFIRM_DELETE.value:
        session.menu_status =  handle_delete_saying(FormStatus.CONFIRM_DELETE, bot, chat_id, session.user_id)

    elif call.data == AppAction.KEEP_SAYING.value:
        session.menu_status =  handle_delete_saying(FormStatus.KEEP_SAYING, bot, chat_id, session.user_id)

    # Menú de la opción 'Ver dichos'
    if call.data == AppAction.HOME_PAGE.value:
        bot_message(bot, chat_id, session.user_id, AppAction.BACK_HOME, general_menu(session.user_id), None)
    
    elif call.data == AppAction.NEXT_PAGE.value:
        if (count_sayings() < session.offset + 10):
            session.offset = 0
        else :
            session.offset = session.offset + 10

        if (session.menu_status == AppAction.WATCHING_SAYINGS.value):
            show_sayings_paginated(bot, chat_id, session.user_id, session.offset)

    elif call.data == AppAction.PREVIOUS_PAGE.value:
        total = count_sayings()

        if (session.offset - 10 < 0):
            session.offset = (total // 10) * 10
        else:
            session.offset -= 10

        show_sayings_paginated(bot, chat_id, session.user_id, session.offset)

if __name__ == "__main__":
    bot.infinity_polling()
