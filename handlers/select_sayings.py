
from telebot import TeleBot
from db.service import get_all_sayings
from ui.enums.help_feedback import HelpFeedback
from ui.menu_options import next_previous_indicators
from ui.messages.messages import build_saying_display, get_help_message

def get_formatted_sayings (offset:int, user_id:int):
    sayings = get_all_sayings(offset=offset)
    sayings_formatted = "".join(build_saying_display(saying, None, user_id) for saying in sayings)
    sayings_helped = f'{sayings_formatted} \n\n {get_help_message(user_id, HelpFeedback.PAGINATION_OPTIONS)}'

    return sayings_helped


def show_sayings_paginated(bot:TeleBot, chat_id: int,user_id:int, offset: int):
    bot.send_message(
        chat_id, 
        get_formatted_sayings(offset, user_id), 
        reply_markup=next_previous_indicators(user_id), 
        parse_mode="Markdown")

    
