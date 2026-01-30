from telebot import TeleBot
from handlers.admin import handle_acept_new_user, handle_reject_new_user
from handlers.configurate_bot import handle_cb_lang_config_button, handle_cb_limit_config_button, handle_cb_show_config, handle_cb_switch_lang
from handlers.delete_sayings import handle_cb_confirm_delete, handle_cb_delete_saying, handle_cb_keep_saying, handle_mss_delete_saying
from handlers.edit_sayings import handle_cb_save_update_saying, handle_cb_update_saying, handle_mss_update_saying
from handlers.new_sayings import handle_cb_new_saying, handle_mss_new_saying
from handlers.pagination import handle_cb_go_home, handle_cb_go_next, handle_cb_go_previous
from handlers.select_sayings import handle_cb_watch_all_sayings
from models.user import User
from ui.enums.app_action import AppAction
from ui.enums.form_status import FormStatus


CALLBACK_DISPATCH = {
    AppAction.INSERT_NEW_SAYING.value: handle_cb_new_saying,
    AppAction.WATCH_ALL_SAYINGS.value: handle_cb_watch_all_sayings,
    AppAction.UPDATE_SAYING.value: handle_cb_update_saying,
    AppAction.EDIT_TITLE.value: handle_cb_update_saying,
    AppAction.EDIT_DESCRIPTION.value: handle_cb_update_saying,
    AppAction.EDIT_AUTHOR.value: handle_cb_update_saying,
    AppAction.EDIT_AUTHOR.value: handle_cb_update_saying,
    AppAction.SAVE_CHANGES.value:handle_cb_save_update_saying,
    AppAction.CONFIG.value: handle_cb_show_config,
    AppAction.LANG_CONFIG_BUTTON.value: handle_cb_lang_config_button,
    AppAction.LIMIT_CONFIG_BUTTON.value: handle_cb_limit_config_button,
    AppAction.DELETE_SAYING.value: handle_cb_delete_saying,
    AppAction.CONFIRM_DELETE.value: handle_cb_confirm_delete,
    AppAction.KEEP_SAYING.value: handle_cb_keep_saying,
    AppAction.HOME_PAGE.value: handle_cb_go_home,
    AppAction.NEXT_PAGE.value: handle_cb_go_next,
    AppAction.PREVIOUS_PAGE.value: handle_cb_go_previous,
    AppAction.LANG_SWITCH.value: handle_cb_switch_lang,
    AppAction.ACEPT_USER.value: handle_acept_new_user,
    AppAction.REJECT_USER.value: handle_reject_new_user

}

MESSAGE_DISPATCH = {
    FormStatus.WAITING_TITLE:handle_mss_new_saying,
    FormStatus.WAITING_DESCRIPTION:handle_mss_new_saying,
    FormStatus.WAITING_AUTHOR:handle_mss_new_saying,
    FormStatus.SEND_SAYING_DELETE:handle_mss_delete_saying,
    FormStatus.WAITING_ID_UPDATE:handle_mss_update_saying,
    FormStatus.EDITING_TITLE:handle_mss_update_saying,
    FormStatus.EDITING_DESCRIPTION:handle_mss_update_saying,
    FormStatus.EDITING_AUTHOR:handle_mss_update_saying,

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
        