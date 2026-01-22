import os
from dotenv import load_dotenv
import telebot
from db.config import check_versions_db
from db.service import count_sayings
from handlers.configurate_bot import handle_configuration
from handlers.delete_sayings import handle_delete_saying
from handlers.edit_sayings import handle_edit_saying
from handlers.new_sayings import handle_new_saying
from handlers.select_sayings import show_sayings_paginated
from ui.enums.app_action import AppAction
from ui.enums.form_status import FormStatus
from ui.menu_options import config_menu, general_menu
from ui.messages.messages import get_message
from utils.bot_message import bot_message
from utils.locale import open_locale, switch_locale


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

menu_status = {}
offset = {}

@bot.message_handler(commands=['start'])
def initialize_bot(message):
    user_id = message.from_user.id

    check_versions_db(user_id)
    open_locale(user_id)

    bot.send_message(message.chat.id, get_message(user_id,AppAction.INTRODUCTION), reply_markup=general_menu(user_id=user_id), parse_mode="Markdown")

# Manejador de respuestas del usuario
@bot.message_handler(content_types=["text"])
def onText(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    message_text = message.text

    if menu_status[user_id] in (
        
        FormStatus.WAITING_TITLE,
        FormStatus.WAITING_DESCRIPTION,
        FormStatus.WAITING_AUTHOR,
    ):
        menu_status[user_id] = handle_new_saying(menu_status[user_id], user_id, bot, chat_id, message_text)

    if (menu_status[user_id] == FormStatus.SEND_SAYING_DELETE):
        handle_delete_saying(menu_status[user_id], bot, chat_id, user_id, message_text)


# Manejador del menú
@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    global menu_status
    global offset

    user_id = call.from_user.id
    chat_id = call.message.chat.id
    # Menú general
    if call.data == AppAction.INSERT_NEW_SAYING.value:
        menu_status[user_id] = handle_new_saying(FormStatus.NEW_SAYING, user_id, bot, chat_id, None)

    elif call.data == AppAction.WATCH_ALL_SAYINGS.value: 
        offset[user_id] = 0
        menu_status[user_id] = AppAction.WATCHING_SAYINGS.value

        show_sayings_paginated(bot, chat_id, user_id,offset[user_id])
    
    elif call.data == AppAction.CONFIG.value: 
        bot_message(bot, chat_id, user_id,  AppAction.CONFIG_MENU,config_menu(user_id), None)

    elif call.data == AppAction.LANG_CONFIG_BUTTON.value:
        menu_status[user_id] = handle_configuration(bot, chat_id, user_id, AppAction.LANG_OPTIONS)
        # bot.send_message(chat_id, "Lenguajes disponibles: ", reply_markup=show_langs_menu(), parse_mode="Markdown" )
    
    elif call.data.startswith("btn_switch_lang_to"):
        order = len (call.data.split("_")) - 1
        new_lang = call.data.split("_")[order]

        switch_locale(user_id, new_lang)
        bot_message(bot, chat_id, user_id, AppAction.BACK_HOME, general_menu(user_id=user_id), None)
        
    
    elif call.data == AppAction.LIMIT_CONFIG_BUTTON.value:
        print("boton para cambiar limit")
        
    # elif call.data == AppAction.SEND_SAYING_EDIT.value:
    #     handle_edit_saying(AppAction.SEND_SAYING_EDIT, bot, chat_id)

    # Lógica de 'Eliminar dichos'
    elif call.data == AppAction.DELETE_SAYING.value: 
        menu_status[user_id] = handle_delete_saying(FormStatus.ASK_ID_DELETE, bot, chat_id, user_id)
    
    elif call.data == AppAction.CONFIRM_DELETE.value:
        menu_status[user_id] =  handle_delete_saying(FormStatus.CONFIRM_DELETE, bot, chat_id, user_id)

    elif call.data == AppAction.KEEP_SAYING.value:
        menu_status[user_id] =  handle_delete_saying(FormStatus.KEEP_SAYING, bot, chat_id, user_id)

    # Menú de la opción 'Ver dichos'
    if call.data == AppAction.HOME_PAGE.value:
        bot_message(bot, chat_id, user_id, AppAction.BACK_HOME, general_menu(user_id=user_id), None)
    
    elif call.data == AppAction.NEXT_PAGE.value:
        if (count_sayings() < offset[user_id] + 10):
            offset[user_id] = 0
        else :
            offset[user_id] = offset[user_id] + 10

        if (menu_status[user_id] == AppAction.WATCHING_SAYINGS.value):
            show_sayings_paginated(bot, chat_id, user_id, offset[user_id])

    elif call.data == AppAction.PREVIOUS_PAGE.value:
        total = count_sayings()

        if (offset[user_id] - 10 < 0):
            offset[user_id] = (total // 10) * 10
        else:
            offset[user_id] -= 10

        show_sayings_paginated(bot, chat_id, user_id, offset[user_id])

if __name__ == "__main__":
    bot.infinity_polling()
