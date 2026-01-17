
from typing import List
from telebot import TeleBot
from db.service import get_all_sayings
from models.saying import Saying
from ui.menu_options import next_previous_indicators
from utils import feedback_saying_item
from utils.locale import LOCALE

def sayings_into_str (sayings: List[Saying]):
    formated_sayings: List[str] = []

    for saying in sayings:
        feedback_title = f'{LOCALE["icons"]["title"]} _{LOCALE["saying"]["title"]}_: {saying.title}'
        feedback_description = f'{LOCALE["icons"]["description"]} _{LOCALE["saying"]["description"]}_: {saying.description}'
        feedback_author = f'{LOCALE["icons"]["author"]} _{LOCALE["saying"]["author"]}_: {saying.author}'
        format_saying = f'''{LOCALE["icons"]["pin"]} *{LOCALE["saying"]["type"]}# {saying.id}:* \n {feedback_title} \n {feedback_description} \n {feedback_author} \n'''
        
        formated_sayings.append(format_saying)

    return  "\n".join(formated_sayings)
    
def build_sayings_message(offset:int) :
    sayings = get_all_sayings(offset=offset)

    sayings_str = sayings_into_str(sayings) 
    return sayings_str

def show_sayings_paginated(bot:TeleBot,user_id: int, sayings: str): 
    bot.send_message(user_id, sayings, parse_mode="Markdown")
    bot.send_message(user_id, f"*{LOCALE["menu"]["pagination_options"]}*", reply_markup=next_previous_indicators(), parse_mode="Markdown")