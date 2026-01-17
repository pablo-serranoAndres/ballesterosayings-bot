from telebot import types
from utils.locale import LOCALE

def general_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn_new = types.InlineKeyboardButton(f'{LOCALE["icons"]["new_saying"]} {LOCALE["menu"]["new_saying"]}', callback_data="btn_insert_new_saying")
    btn_see = types.InlineKeyboardButton(f'{LOCALE["icons"]["select_all_sayings"]} {LOCALE["menu"]["select_all_sayings"]}', callback_data="btn_select_all_sayings")
    btn_delete = types.InlineKeyboardButton(f'{LOCALE["icons"]["delete"]} {LOCALE["menu"]["delete_saying"]}', callback_data="btn_delete_saying")
    btn_update = types.InlineKeyboardButton(f'{LOCALE["icons"]["update"]} {LOCALE["menu"]["update_saying"]}', callback_data="btn_update_saying")
    btn_config = types.InlineKeyboardButton(f'{LOCALE["icons"]["configuration"]} {LOCALE["menu"]["configuration"]}', callback_data="btn_config")
    btn_help = types.InlineKeyboardButton(f'{LOCALE["icons"]["help"]} {LOCALE["menu"]["help"]}', callback_data="btn_help")

    markup.add(btn_new, btn_see, btn_delete, btn_update, btn_config, btn_help)

    return markup
def go_home_indicator(): 
    markup = types.InlineKeyboardMarkup(row_width=1)

    btn_home = types.InlineKeyboardButton(f'{LOCALE["icons"]["home"]} {LOCALE["menu"]["home"]}', callback_data="btn_home_page")

    markup.add(btn_home)

    return markup

def saying_item(): 
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn_delete = types.InlineKeyboardButton(f'{LOCALE["icons"]["delete"]} {LOCALE["menu"]["delete_saying"]}', callback_data="btn_delete")
    btn_edit = types.InlineKeyboardButton(f'{LOCALE["icons"]["update"]} {LOCALE["menu"]["update_saying"]}', callback_data="btn_edit")

    markup.add(btn_edit, btn_delete)

    return markup


def next_previous_indicators(): 
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn_next_page = types.InlineKeyboardButton(f'{LOCALE["icons"]["next"]} {LOCALE["menu"]["next_page"]}', callback_data="btn_next_page")
    btn_previous_page = types.InlineKeyboardButton(f'{LOCALE["icons"]["previous"]} {LOCALE["menu"]["previous_page"]}', callback_data="btn_previous_page")
    btn_home = types.InlineKeyboardButton(f'{LOCALE["icons"]["home"]} {LOCALE["menu"]["home"]}', callback_data="btn_home_page")

    markup.add(btn_previous_page, btn_next_page, btn_home)

    return markup

def saying_item_delete(): 
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn_keep_saying = types.InlineKeyboardButton(f'{LOCALE["icons"]["success"]} {LOCALE["forms"]["delete"]["keep_saying"]}', callback_data="btn_confirm_keep_saying")
    btn_delete_saying = types.InlineKeyboardButton(f'{LOCALE["icons"]["delete"]} {LOCALE["forms"]["delete"]["delete_saying"]}', callback_data="btn_confirm_delete_saying")

    markup.add(btn_keep_saying, btn_delete_saying)

    return markup

