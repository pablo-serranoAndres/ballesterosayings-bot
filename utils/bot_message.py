from telebot import REPLY_MARKUP_TYPES, TeleBot
from config import bot
from models.saying import Saying
from enums.app_action import AppAction
from models.user import User
from ui.messages import build_saying_display, get_markup, get_message

def bot_message(
        session: User
            # bot:TeleBot, 
            # chat_id:int, 
            # user_id: int, 
            # app_action:  AppAction,
            # markup: REPLY_MARKUP_TYPES = None, 
            # saying: Saying = None
            ):
      
      text = get_message(session.user_id, session.app_action)
      markup = get_markup(session.user_id, session.app_action)

      

      # if (saying) :
      #       text = build_saying_display(saying, app_action, user_id)
      
      # else :
      #       text = get_message(user_id, app_action)
            

      bot.send_message(
            chat_id,
            text,
            reply_markup=markup,
            parse_mode="Markdown"
            )