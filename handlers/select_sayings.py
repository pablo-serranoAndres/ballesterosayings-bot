
from typing import List
from telebot import TeleBot
from db.service import get_all_sayings
from models.saying import Saying
from ui.menu_options import next_previous_indicators
from ui.messages.messages import build_saying_display
from utils.locale import LOCALE

def sayings_into_str (sayings: List[Saying]):
    formatted_sayings: List[str] = []

    for saying  in sayings:
        formatted_sayings.append(build_saying_display(saying, None))
        
    return  "\n".join(formatted_sayings)
    
def build_sayings_message(offset:int) :
    sayings = get_all_sayings(offset=offset)

    sayings_str = sayings_into_str(sayings) 
    return sayings_str

def show_sayings_paginated(bot:TeleBot, chat_id: int, offset: int):
    text = f'{build_sayings_message(offset)}\n\n{LOCALE["icons"]["help"]} {LOCALE["menu"]["pagination_options"]}'
    bot.send_message(chat_id, text, reply_markup=next_previous_indicators(), parse_mode="Markdown")