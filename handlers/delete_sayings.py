from telebot import TeleBot

from db.service import delete_saying_by_id, get_saying_by_id
from ui.menu_options import saying_item_delete
from utils.locale import LOCALE

saying_to_eliminate = {}

def ask_id_eliminate(bot: TeleBot, ask_id_message:str, chat_id: int ):
    bot.send_message(
        chat_id,
        ask_id_message,
        parse_mode="Markdown")
    
    return "waiting_id_eliminate"

def send_saying_for_confirmation(bot, message, chat_id, user_id):
    saying_selected_to_eliminate = get_saying_by_id(message, user_id)
    saying_to_eliminate[user_id] =  saying_selected_to_eliminate

    message_elimination = f'''
{LOCALE["forms"]["delete"]["delete_confirmation"]}
{LOCALE["icons"]["pin"]} {LOCALE["saying"]["type"]}  #{saying_selected_to_eliminate.id}
{LOCALE["icons"]["title"]} {LOCALE["saying"]["title"]} : {saying_selected_to_eliminate.title}
{LOCALE["icons"]["description"]} {LOCALE["saying"]["description"]} : {saying_selected_to_eliminate.description}
{LOCALE["icons"]["author"]} {LOCALE["saying"]["author"]} : {saying_selected_to_eliminate.author}
'''

    bot.send_message(
        chat_id,
        message_elimination,
        reply_markup=saying_item_delete(),
        parse_mode="Markdown")

    #print(f"Eliminar dicho: {saying_to_delete.title}?")

def delete_confirmed (bot, user_id, chat_id) :
    delete_saying_by_id(user_id, saying_to_eliminate[user_id].id)

    bot.send_message(
        chat_id,
        LOCALE["forms"]["delete"]["delete_confirmed"],
        parse_mode="Markdown")