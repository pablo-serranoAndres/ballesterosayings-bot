from enums.app_action import AppAction
from models.saying import Saying
from models.user import User
from ui.message_factory import display_saying
from utils import bot_message


new_saying = dict[User, Saying] = {}

def handle_cb_new_saying(session: User):
    session.app_action = AppAction.INSERTING_NEW_SAYING
    new_saying[session] = Saying (
        title = "",
        description = "",
        author = "",
    )
    bot_message(session, display_saying(session.lang, new_saying, "NEW"))

def handle_cb_ns_adding_values(session:User, call_data):
    session.app_action = call_data
    bot_message(session)

def handle_msg_new_saying(message, session: User):
    if(session.app_action == AppAction.CB_NS_ADD_TITLE):
        new_saying[session.user_id].title = message.text

    elif(session.app_action == AppAction.CB_NS_ADD_DESCRIPTION):
        new_saying[session.user_id].description = message.text

    elif(session.app_action == AppAction.CB_NS_ADD_AUTHOR):
        new_saying[session.user_id].author = message.text
    
    
    bot_message(
        session, 
        display_saying(session.lang, new_saying[session.user_id],"NEW"))
