from telebot import TeleBot
from handlers.new_sayings import handle_cb_new_saying
from models.user import User
from enums.app_action import AppAction


CALLBACK_DISPATCH = {
    AppAction.CB_INSERT_NEW_SAYING.value: handle_cb_new_saying,
    
}

MESSAGE_DISPATCH = {


}

def dispatch_callback(call, bot:TeleBot, session: User): 
    call_data_splitted = call.data.split(";")
    dispatch_key = call_data_splitted[0]
    
    aditional_params = call_data_splitted[1] if (len (call_data_splitted) > 1) else None
    
    handler = CALLBACK_DISPATCH.get(dispatch_key)
    chat_id = call.message.chat.id

    if handler:
        handler(session, bot, chat_id, aditional_params)

def dispatch_message(message, bot:TeleBot, session: User):
    handler = MESSAGE_DISPATCH.get(session.menu_status)

    if handler:
        handler(message, bot, session)
        