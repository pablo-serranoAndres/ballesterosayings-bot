from telebot import REPLY_MARKUP_TYPES, TeleBot
from models.saying import Saying
from ui.enums.app_action import AppAction
from ui.enums.form_status import FormStatus
from ui.messages.messages import build_saying_display, get_message

def bot_message(
            bot:TeleBot, 
            chat_id:int, 
            user_id: int, 
            form_status:FormStatus | AppAction,
            markup: REPLY_MARKUP_TYPES = None, 
            saying: Saying = None):
      text = ""

      if (saying) :
            text = build_saying_display(saying, form_status, user_id)
            
            # if (form_status == FormStatus.SEND_SAYING_DELETE) :
            #       text = build_saying_display(saying, form_status, user_id)
            # elif (form_status == FormStatus.SEND_SAYING_UPDATE) :
            #       text = build_saying_display(saying, form_status, user_id)

      else :
            text = get_message(user_id, form_status)
            

      bot.send_message(
            chat_id,
            text,
            reply_markup=markup,
            parse_mode="Markdown"
            )