from telebot import TeleBot
from models.user import User

new_saying = {}

def handle_cb_new_saying(session: User, bot:TeleBot, chat_id:int, aditional_params:str):
    # new_saying[session.user_id] = Saying("","","","")
    print("handle_cb_new_saying")
    
