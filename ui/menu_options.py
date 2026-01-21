from telebot import types
from ui.enums.app_action import AppAction
from ui.messages.messages import get_message

def general_menu(user_id: int):
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn_new = types.InlineKeyboardButton(get_message(user_id, AppAction.INSERT_NEW_SAYING), callback_data=AppAction.INSERT_NEW_SAYING.value)
    btn_see = types.InlineKeyboardButton(get_message(user_id, AppAction.WATCH_ALL_SAYINGS), callback_data=AppAction.WATCH_ALL_SAYINGS.value)
    btn_delete = types.InlineKeyboardButton(get_message(user_id, AppAction.DELETE_SAYING), callback_data=AppAction.DELETE_SAYING.value)
    btn_update = types.InlineKeyboardButton(get_message(user_id, AppAction.UPDATE_SAYING), callback_data=AppAction.UPDATE_SAYING.value)
    btn_config = types.InlineKeyboardButton(get_message(user_id, AppAction.CONFIG), callback_data=AppAction.CONFIG.value)
    #btn_help = types.InlineKeyboardButton(f'{LOCALE["icons"]["help"]} {LOCALE["menu"]["help"]}', callback_data="btn_help")

    markup.add(btn_see, btn_delete, btn_update, btn_config, btn_new)
    return markup

def go_home_indicator(user_id: int): 
    markup = types.InlineKeyboardMarkup(row_width=1)

    btn_home = types.InlineKeyboardButton(get_message(user_id, AppAction.HOME_PAGE), callback_data=AppAction.HOME_PAGE.value)

    markup.add(btn_home)
    return markup

def next_previous_indicators(user_id: int): 
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn_next_page = types.InlineKeyboardButton(get_message(user_id, AppAction.NEXT_PAGE), callback_data=AppAction.NEXT_PAGE.value)
    btn_previous_page = types.InlineKeyboardButton(get_message(user_id, AppAction.PREVIOUS_PAGE), callback_data=AppAction.PREVIOUS_PAGE.value)
    btn_home = types.InlineKeyboardButton(get_message(user_id, AppAction.HOME_PAGE), callback_data=AppAction.HOME_PAGE.value)

    markup.add(btn_previous_page, btn_next_page, btn_home)
    return markup

def saying_item_delete(user_id: int): 
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn_keep_saying = types.InlineKeyboardButton(get_message(user_id, AppAction.KEEP_SAYING), callback_data=AppAction.KEEP_SAYING.value)
    btn_delete_saying = types.InlineKeyboardButton(get_message(user_id, AppAction.CONFIRM_DELETE), callback_data=AppAction.CONFIRM_DELETE.value)

    markup.add(btn_keep_saying, btn_delete_saying)
    return markup

def saying_item_edit(user_id: int): 
    markup = types.InlineKeyboardMarkup(row_width=4)

    btn_edit_title = types.InlineKeyboardButton(get_message(user_id,AppAction.EDIT_TITLE), callback_data=AppAction.EDIT_TITLE.value)
    btn_edit_description = types.InlineKeyboardButton(get_message(user_id,AppAction.EDIT_DESCRIPTION), callback_data=AppAction.EDIT_DESCRIPTION.value)
    btn_edit_author = types.InlineKeyboardButton(get_message(user_id,AppAction.EDIT_AUTHOR), callback_data=AppAction.EDIT_AUTHOR.value)
    btn_home = types.InlineKeyboardButton(get_message(user_id, AppAction.HOME_PAGE), callback_data=AppAction.HOME_PAGE.value)

    markup.add(btn_edit_title, btn_edit_description, btn_edit_author, btn_home)
    return markup

def config_menu(user_id: int): 
    markup = types.InlineKeyboardMarkup(row_width=1)

    btn_lang_switch_config = types.InlineKeyboardButton(get_message(user_id, AppAction.LIMIT_CONFIG_BUTTON), callback_data=AppAction.LIMIT_CONFIG_BUTTON.value)
    btn_query_limit_config = types.InlineKeyboardButton(get_message(user_id, AppAction.WATCHING_SAYINGS), callback_data=AppAction.LIMIT_CONFIG_BUTTON.value)

    markup.add(btn_lang_switch_config, btn_query_limit_config)

    return markup

    