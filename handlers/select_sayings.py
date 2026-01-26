
from telebot import TeleBot
from db.service import get_all_sayings
from models.user import User
from ui.enums.help_feedback import HelpFeedback
from ui.menu_options import next_previous_indicators
from ui.messages.messages import build_saying_display, get_help_message

def get_formatted_sayings (session:User):
    sayings = get_all_sayings(session=session)
    sayings_formatted = "".join(build_saying_display(saying, None, session.user_id) for saying in sayings)
    sayings_helped = f'{sayings_formatted} \n\n {get_help_message(session.user_id, HelpFeedback.PAGINATION_OPTIONS)}'

    return sayings_helped


def show_sayings_paginated(bot:TeleBot, chat_id: int, session:User):
    bot.send_message(
        chat_id, 
        get_formatted_sayings(session), 
        reply_markup=next_previous_indicators(session.user_id), 
        parse_mode="Markdown")

    
