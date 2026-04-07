from telebot import TeleBot
from handlers.admin import *
from handlers.configurate_bot import *
from handlers.delete_sayings import *
from handlers.edit_sayings import *
from handlers.new_sayings import *
from handlers.pagination import *
from handlers.select_sayings import *
from models.user import User
from enums.app_action import AppAction
from enums.form_status import AppAction


CALLBACK_DISPATCH = {
    AppAction.INSERT_NEW_SAYING.value: handle_cb_new_saying,
    
}

MESSAGE_DISPATCH = {
    AppAction.WAITING_TITLE:handle_mss_new_saying,
    AppAction.WAITING_DESCRIPTION:handle_mss_new_saying,
    AppAction.WAITING_AUTHOR:handle_mss_new_saying,
    AppAction.SEND_SAYING_DELETE:handle_mss_delete_saying,
    AppAction.WAITING_ID_UPDATE:handle_mss_update_saying,
    AppAction.EDITING_TITLE:handle_mss_update_saying,
    AppAction.EDITING_DESCRIPTION:handle_mss_update_saying,
    AppAction.EDITING_AUTHOR:handle_mss_update_saying,

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
        