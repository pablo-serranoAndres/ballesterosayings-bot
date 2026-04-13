from handlers.new_saying import *
from models.user import User
from enums.app_action import AppAction


CALLBACK_DISPATCH = {
    AppAction.CB_INSERT_NEW_SAYING.value: handle_cb_new_saying,
    
    AppAction.CB_NS_ADD_TITLE.value: handle_cb_ns_adding_values,    
    AppAction.CB_NS_ADD_DESCRIPTION.value: handle_cb_ns_adding_values,    
    AppAction.CB_NS_ADD_AUTHOR.value: handle_cb_ns_adding_values,
    AppAction.CB_NS_SAVE.value: handle_cb_ns_adding_values,
    AppAction.CB_NS_DISCARD.value: handle_cb_ns_adding_values,
}

MESSAGE_DISPATCH = {
    AppAction.CB_NS_ADD_TITLE.value: handle_cb_ns_adding_values,    
    AppAction.CB_NS_ADD_DESCRIPTION.value: handle_cb_ns_adding_values,    
    AppAction.CB_NS_ADD_AUTHOR.value: handle_cb_ns_adding_values,    

}

def dispatch_callback(call, session: User): 
    call_data_splitted = call.data.split(";")
    dispatch_key = call_data_splitted[0]
    
    # aditional_params = call_data_splitted[1] if (len (call_data_splitted) > 1) else None
    
    handler = CALLBACK_DISPATCH.get(dispatch_key)
    # chat_id = call.message.chat.id

    if handler:
        handler(session, call.data)

def dispatch_message(message, session: User):
    handler = MESSAGE_DISPATCH.get(session.app_action)

    if handler:
        handler(message, session)
        