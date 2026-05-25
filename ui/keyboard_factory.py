
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
        callback_data=AppAction.CB_INSERT_NEW_SAYING.value)
    
    btn_handle_sayings = types.InlineKeyboardButton(
        get_message(user_id, AppAction.BTN_HANDLE_SAYINGS), 
        callback_data=AppAction.CB_HANDLE_SAYINGS.value)
    
    btn_bot_configuration = types.InlineKeyboardButton(
        get_message(user_id, AppAction.BTN_BOT_CONFIGURATION), 
        callback_data=AppAction.CB_BOT_CONFIGURATION.value)

    markup.add(btn_new_saying, btn_handle_sayings, btn_bot_configuration)
    return markup

def new_saying_form(user_id: int):
    markup = types.InlineKeyboardButton(row_width=3)
    
    btn_ns_add_title = types.InlineKeyboardButton(
        get_message(user_id, AppAction.BTN_NSY_ADD_TITLE),
        callback_data=AppAction.CB_NSY_ADD_TITLE.value)
    
    btn_ns_add_description = types.InlineKeyboardButton(
        get_message(user_id, AppAction.BTN_NSY_ADD_DESCRIPTION),
        callback_data=AppAction.CB_SY_ADD_DESCRIPTION.value)
    
    btn_ns_add_author = types.InlineKeyboardButton(
        get_message(user_id, AppAction.BTN_NSY_ADD_AUTHOR),
        callback_data=AppAction.CB_NSY_ADD_AUTHOR.value)
    
    btn_ns_save_saying = types.InlineKeyboardButton(
        get_message(user_id, AppAction.BTN_NSY_SAVE_SAYING),
        callback_data=AppAction.CB_NSY_SAVE_SAYING.value)
    
    markup.add(btn_ns_add_title, btn_ns_add_description, btn_ns_add_author)
    return markup