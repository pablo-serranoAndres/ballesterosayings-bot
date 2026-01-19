from telebot import REPLY_MARKUP_TYPES, TeleBot
from models.saying import Saying
from ui.enums.form_status import FormStatus
from ui.messages.messages import MESSAGES, build_saying_display
from utils.locale import LOCALE

def bot_message(
            bot:TeleBot, 
            chat_id:int, 
            form_status:FormStatus, 
            markup: REPLY_MARKUP_TYPES = None, 
            saying: Saying = None):
      text = ""
      if (saying) :
            if (form_status == FormStatus.SEND_SAYING_DELETE) :
                  text = build_saying_display(saying, form_status)

      else :
            text = MESSAGES.get(form_status, LOCALE["feedback"]["error"])

      bot.send_message(
            chat_id,
            text,
            reply_markup=markup,
            parse_mode="Markdown"
            )