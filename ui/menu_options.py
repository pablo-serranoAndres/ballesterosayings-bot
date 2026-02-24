import os
from typing import List
from telebot import types
from models.saying import Saying
from ui.enums.app_action import AppAction
from ui.messages.messages import  get_lang_info, get_message
from utils.locale import get_available_langs

def general_menu(user_id: int):
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn_new = types.InlineKeyboardButton(get_message(user_id, AppAction.INSERT_NEW_SAYING), callback_data=AppAction.INSERT_NEW_SAYING.value)
    btn_see = types.InlineKeyboardButton(get_message(user_id, AppAction.WATCH_ALL_SAYINGS), callback_data=AppAction.WATCH_ALL_SAYINGS.value)
    btn_delete = types.InlineKeyboardButton(get_message(user_id, AppAction.DELETE_SAYING), callback_data=AppAction.DELETE_SAYING.value)
    btn_update = types.InlineKeyboardButton(get_message(user_id, AppAction.UPDATE_SAYING), callback_data=AppAction.UPDATE_SAYING.value)
    btn_config = types.InlineKeyboardButton(get_message(user_id, AppAction.CONFIG), callback_data=AppAction.CONFIG.value)
    btn_user_admin = types.InlineKeyboardButton(get_message(user_id, AppAction.USER_ADMIN), callback_data=AppAction.USER_ADMIN.value)

    if (user_id == int(os.getenv("ADMIN_ID"))):
        markup.add(btn_see, btn_delete, btn_update, btn_config, btn_new, btn_user_admin)
    
    else:
        markup.add(btn_see, btn_update, btn_config, btn_new) 

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

def saying_item_edit(user_id: int, saying_id: int): 
    markup = types.InlineKeyboardMarkup(row_width=3)

    btn_edit_title = types.InlineKeyboardButton(get_message(user_id,AppAction.EDIT_TITLE), callback_data=f'{AppAction.EDIT_TITLE.value};title-{saying_id}')
    btn_edit_description = types.InlineKeyboardButton(get_message(user_id,AppAction.EDIT_DESCRIPTION), callback_data=f'{AppAction.EDIT_DESCRIPTION.value};description-{saying_id}')
    btn_edit_author = types.InlineKeyboardButton(get_message(user_id,AppAction.EDIT_AUTHOR), callback_data=f'{AppAction.EDIT_AUTHOR.value};author-{saying_id}')
    
    btn_home = types.InlineKeyboardButton(get_message(user_id, AppAction.NOT_SAVE), callback_data=AppAction.HOME_PAGE.value)
    btn_save = types.InlineKeyboardButton(get_message(user_id, AppAction.SAVE_CHANGES), callback_data=AppAction.SAVE_CHANGES.value)
    
    markup.add(btn_edit_title, btn_edit_description, btn_edit_author, btn_home, btn_save)
    return markup

def config_menu(user_id: int): 
    markup = types.InlineKeyboardMarkup(row_width=1)

    # btn_query_limit_config = types.InlineKeyboardButton(get_message(user_id, AppAction.LIMIT_CONFIG_BUTTON), callback_data=AppAction.LIMIT_CONFIG_BUTTON.value)
    btn_lang_switch_config = types.InlineKeyboardButton(get_message(user_id, AppAction.LANG_CONFIG_BUTTON), callback_data=AppAction.LANG_CONFIG_BUTTON.value)
    btn_home = types.InlineKeyboardButton(get_message(user_id, AppAction.HOME_PAGE), callback_data=AppAction.HOME_PAGE.value)

    markup.add(btn_lang_switch_config,btn_home)

    return markup

def available_langs(user_id:int):
    markup = types.InlineKeyboardMarkup(row_width=1)
    available_langs = get_available_langs()

    for lang in available_langs:
        markup.add(
            types.InlineKeyboardButton(
                get_lang_info(user_id, lang),
                callback_data=f'btn_switch_lang_to;{lang}'
            )
        )
    btn_home = types.InlineKeyboardButton(get_message(user_id, AppAction.HOME_PAGE), callback_data=AppAction.HOME_PAGE.value)
    markup.add(btn_home)

    return markup
        
def acept_reject_users(user_id: int, new_user_id):
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn_acept_user = types.InlineKeyboardButton(get_message(user_id, AppAction.ACEPT_USER), callback_data=f'{AppAction.ACEPT_USER.value};acept-{new_user_id}')
    btn_reject_user = types.InlineKeyboardButton(get_message(user_id, AppAction.REJECT_USER), callback_data=f'{AppAction.REJECT_USER.value};reject-{new_user_id}')
        
    markup.add(btn_acept_user, btn_reject_user)

    return markup

def confirm_new_saying(user_id: int, new_saying_id):
    markup = types.InlineKeyboardMarkup(row_width=3)

    btn_save = types.InlineKeyboardButton(get_message(user_id, AppAction.SAVE_NEW_SAYING), callback_data=f'{AppAction.SAVE_NEW_SAYING.value};save-{new_saying_id}')
    btn_edit = types.InlineKeyboardButton(get_message(user_id, AppAction.EDIT_NEW_SAYING), callback_data=f'{AppAction.EDIT_NEW_SAYING.value};edit-{new_saying_id}')
    btn_delete = types.InlineKeyboardButton(get_message(user_id, AppAction.DELETE_NEW_SAYING), callback_data=f'{AppAction.DELETE_NEW_SAYING.value};delete-{new_saying_id}')

    markup.add(btn_save, btn_edit, btn_delete)
    return markup

def sayings_to_edit (user_id: int, sayings: List[Saying]):
    markup = types.InlineKeyboardMarkup(row_width=4)

    for saying in sayings: 
        markup.add(
            types.InlineKeyboardButton(
                saying.id, 
                callback_data=f'{AppAction.EDITING_SAYING.value};{saying.id}'
            )
        )

    return markup
