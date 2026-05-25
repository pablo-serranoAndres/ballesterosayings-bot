from enum import Enum


class AppAction(Enum):
    #ESTADOS
    WELCOME_MENU = "welcome_menu"
    MAIN_MENU = "main_menu"
    REGISTERING_USER = "registering_user"
    USER_NOT_AUTORIZATED = "user_not_autorizated"


    #BOTONES
    BTN_INSERT_NEW_SAYING = "btn_insert_new_saying"
    BTN_HANDLE_SAYINGS = "btn_handle_sayings"    
    BTN_BOT_CONFIGURATION = "btn_bot_configuration"
    BTN_HANDLE_USERS = "btn_handle_users"

    BTN_NSY_ADD_TITLE = "btn_nsy_add_title"
    BTN_NSY_ADD_DESCRIPTION = "btn_nsy_add_description"
    BTN_NSY_ADD_AUTHOR = "btn_nsy_add_author"

    #CALLBACKS
    CB_INSERT_NEW_SAYING = "cb_insert_new_saying"
    CB_HANDLE_SAYINGS = "cb_handle_sayings"
    CB_BOT_CONFIGURATION = "cb_bot_configuration"
    CB_HANDLE_USERS = "cb_handle_users"

    CB_NSY_ADD_TITLE = "cb_nsy_add_title"
    CB_NSY_ADD_DESCRIPTION = "cb_nsy_add_description"
    CB_NSY_ADD_AUTHOR = "cb_nsy_add_author"
