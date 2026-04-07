from enum import Enum


class AppAction(Enum):
    #ESTADOS
    WELCOME_MENU = "welcome_menu"
    MAIN_MENU = "main_menu"
    REGISTERING_USER = "registering_user"


    #BOTONES
    BTN_INSERT_NEW_SAYING = "btn_insert_new_saying"
    BTN_HANDLE_SAYINGS = "btn_handle_sayings"    
    BTN_BOT_CONFIGURATION = "btn_bot_configuration"
    BTN_HANDLE_USERS = "btn_handle_users"

    #CALLBACKS
    CB_INSERT_NEW_SAYING = "cb_insert_new_saying"
    CB_HANDLE_SAYINGS = "cb_handle_sayings"
    CB_BOT_CONFIGURATION = "cb_bot_configuration"
    CB_HANDLE_USERS = "cb_handle_users"
