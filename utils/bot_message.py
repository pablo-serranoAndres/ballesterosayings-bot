from config import bot
from models.user import User
from services.messages import  get_markup, get_text

def bot_message(session:User, text:str = None):
      bot.send_message(
            chat_id=session.user_id,
            text=text or get_text(session.lang,
                          session.menu_status),
            reply_markup=get_markup(session.user_id, 
                                    session.app_action),
            parse_mode="Markdown"
            )