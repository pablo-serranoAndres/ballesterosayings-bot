import os
import telebot
from dotenv import load_dotenv
from db.config import check_versions_db
from db.service import count_sayings
from handlers.delete_sayings import ask_id_eliminate, delete_confirmed, send_saying_for_confirmation
from handlers.new_sayings import handle_new_saying
from handlers.select_sayings import build_sayings_message, show_sayings_paginated
from ui.menu_options import general_menu
from utils.locale import LOCALE


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
check_versions_db()

menu_status = {}
offset = {}

@bot.message_handler(commands=['start'])
def initialize_bot(message):
    bot.send_message(message.chat.id, LOCALE["introduction"], reply_markup=general_menu(), parse_mode="Markdown")

# Manejador de respuestas del usuario
@bot.message_handler(content_types=["text"])
def onText(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    message_text = message.text
    status = menu_status.get(user_id)

    if menu_status[user_id] in ("waiting_new_saying_title", "waiting_new_saying_description", "waiting_new_saying_author", "new_saying_terminated"):
        menu_status[user_id] = handle_new_saying(status, user_id, bot, chat_id, message_text)

    if (menu_status[user_id] == "waiting_id_eliminate"):
        send_saying_for_confirmation(bot, message_text, chat_id, user_id=user_id)



# Manejador del menú
@bot.callback_query_handler(func=lambda call:True)
def callback_query(call): 
    global menu_status
    global offset

    user_id = call.from_user.id
    chat_id = call.message.chat.id
    # Menú general
    if call.data == "btn_insert_new_saying":
        menu_status[user_id] = handle_new_saying("ask_title", user_id, bot, chat_id, "")

    elif call.data == "btn_select_all_sayings": 
        offset[user_id] = 0
        menu_status[user_id] = "watching_sayings"

        show_sayings_paginated(bot, user_id, build_sayings_message(offset[user_id]))

    elif call.data == "btn_delete_saying": 
        menu_status[user_id] = ask_id_eliminate(bot, LOCALE["forms"]["delete"]["ask_saying_id"], chat_id)
    
    elif call.data == "btn_confirm_keep_saying":
        bot.send_message(user_id, LOCALE["introduction"], reply_markup=general_menu(), parse_mode="Markdown")

    elif call.data == "btn_confirm_delete_saying":
        delete_confirmed(bot, user_id, chat_id)
        bot.send_message(user_id, LOCALE["introduction"], reply_markup=general_menu(), parse_mode="Markdown")



    elif call.data == "btn_update_saying": 
        bot.answer_callback_query(call.id, "update_saying")

    # Menú de la opción 'Ver dichos'
    if call.data == "btn_home_page":
        bot.send_message(user_id, LOCALE["introduction"], reply_markup=general_menu(), parse_mode="Markdown")
    
    elif call.data == "btn_next_page":
        if (count_sayings() < offset[user_id] + 10):
            offset[user_id] = 0
        else :
            offset[user_id] = offset[user_id] + 10

        if (menu_status[user_id] == "watching_sayings"):
            show_sayings_paginated(bot, user_id, build_sayings_message(offset[user_id]))

    elif call.data == "btn_previous_page":
        total = count_sayings()

        if (offset[user_id] - 10 < 0):
            offset[user_id] = (total // 10) * 10
        else:
            offset[user_id] -= 10

        show_sayings_paginated(bot, user_id, build_sayings_message(offset[user_id]))

if __name__ == "__main__":
    bot.infinity_polling()
