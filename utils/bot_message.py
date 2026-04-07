from telebot import REPLY_MARKUP_TYPES, TeleBot
from config import bot
from models.saying import Saying
from enums.app_action import AppAction
from ui.messages import build_saying_display, get_message

def bot_message(
            # bot:TeleBot, 
            chat_id:int, 
            user_id: int, 
            app_action:  AppAction,
            markup: REPLY_MARKUP_TYPES = None, 
            saying: Saying = None):
      text = ""

      if (saying) :
            text = build_saying_display(saying, app_action, user_id)
      
      else :
            text = get_message(user_id, app_action)
            

      bot.send_message(
            chat_id,
            text,
            reply_markup=markup,
            parse_mode="Markdown"
            )