
from telebot import types
from config import ADMIN_ID
from enums.app_action import AppAction
from models.user import User
from services.messages import get_text


def general_menu(session: User):
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn_new_saying = types.InlineKeyboardButton(
        get_text(session.lang, AppAction.BTN_INSERT_NEW_SAYING), 
        callback_data=AppAction.CB_INSERT_NEW_SAYING.value)
    
    btn_handle_sayings = types.InlineKeyboardButton(
        get_text(session.lang, AppAction.BTN_HANDLE_SAYINGS), 
        callback_data=AppAction.CB_HANDLE_SAYINGS.value)
    
    btn_bot_configuration = types.InlineKeyboardButton(
        get_text(session.lang, AppAction.BTN_BOT_CONFIGURATION), 
        callback_data=AppAction.CB_BOT_CONFIGURATION.value)
    
    if session.user_id is ADMIN_ID :
        btn_handle_users = types.InlineKeyboardButton(
            get_text(session.lang, AppAction.BTN_HANDLE_USERS), 
            callback_data=AppAction.CB_HANDLE_USERS.value)
        markup.add(btn_new_saying, btn_handle_sayings, btn_bot_configuration, btn_handle_users)
    else:
        markup.add(btn_new_saying, btn_handle_sayings, btn_bot_configuration)

    return markup

def new_saying(session: User):
    markup = types.InlineKeyboardMarkup(row_width=3)
    
    btn_ns_add_title = types.InlineKeyboardButton(
        get_text(session.lang, AppAction.BTN_NS_ADD_TITLE),
        callback_data= AppAction.CB_NS_ADD_TITLE.value
    )

    btn_ns_add_description = types.InlineKeyboardButton(
        get_text(session.lang, AppAction.BTN_NS_ADD_DESCRIPTION),
        callback_data= AppAction.CB_NS_ADD_DESCRIPTION.value
    )

    btn_ns_add_author = types.InlineKeyboardButton(
        get_text(session.lang, AppAction.BTN_NS_ADD_AUTHOR),
        callback_data= AppAction.CB_NS_ADD_AUTHOR.value
    )

    btn_ns_save = types.InlineKeyboardButton(
        get_text(session.lang, AppAction.BTN_NS_SAVE),
        callback_data= AppAction.CB_NS_SAVE.value
    ) 

    btn_ns_discard = types.InlineKeyboardButton(
        get_text(session.lang, AppAction.BTN_NS_DISCARD),
        callback_data= AppAction.CB_NS_DISCARD.value
    ) 

    markup.add(btn_ns_add_title, 
               btn_ns_add_description, 
               btn_ns_add_author,
               btn_ns_save,
               btn_ns_discard)
    return markup
