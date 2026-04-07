
from telebot import types
from enums.app_action import AppAction
from ui.messages import get_message


def admin_general_menu(user_id: int):
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn_new_saying = types.InlineKeyboardButton(
        get_message(user_id, AppAction.BTN_INSERT_NEW_SAYING), 
        callback_data=AppAction.CB_INSERT_NEW_SAYING.value)
    
    btn_handle_sayings = types.InlineKeyboardButton(
        get_message(user_id, AppAction.BTN_HANDLE_SAYINGS), 
        callback_data=AppAction.CB_HANDLE_SAYINGS.value)
    
    btn_bot_configuration = types.InlineKeyboardButton(
        get_message(user_id, AppAction.BTN_BOT_CONFIGURATION), 
        callback_data=AppAction.CB_BOT_CONFIGURATION.value)
    
    btn_handle_users = types.InlineKeyboardButton(
        get_message(user_id, AppAction.BTN_HANDLE_USERS), 
        callback_data=AppAction.CB_HANDLE_USERS.value)


    markup.add(btn_new_saying, btn_handle_sayings, btn_bot_configuration, btn_handle_users)
    return markup

def general_menu(user_id: int):
    markup = types.InlineKeyboardMarkup(row_width=3)

    btn_new_saying = types.InlineKeyboardButton(
        get_message(user_id, AppAction.BTN_INSERT_NEW_SAYING), 
        callback_data=AppAction.CB_INSERT_NEW_SAYING)
    
    btn_handle_sayings = types.InlineKeyboardButton(
        get_message(user_id, AppAction.BTN_HANDLE_SAYINGS), 
        callback_data=AppAction.CB_HANDLE_SAYINGS)
    
    btn_bot_configuration = types.InlineKeyboardButton(
        get_message(user_id, AppAction.BTN_BOT_CONFIGURATION), 
        callback_data=AppAction.CB_BOT_CONFIGURATION)

    markup.add(btn_new_saying, btn_handle_sayings, btn_bot_configuration)
    return markup
