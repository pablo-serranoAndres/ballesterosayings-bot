from enum import Enum


class AppAction(Enum):
    #ESTADOS
    WELCOME_MENU = "welcome_menu"
    MAIN_MENU = "main_menu"
    REGISTERING_USER = "registering_user"

    INSERTING_NEW_SAYING = "inserting_new_saying"
    # INS_ADDING_TITLE = "ins_adding_title"
    # INS_ADDING_DESCRIPTION = "ins_adding_desription"
    # INS_ADDING_AUTHOR = "ins_adding_author"

    #BOTONES
    BTN_INSERT_NEW_SAYING = "btn_insert_new_saying"
    BTN_HANDLE_SAYINGS = "btn_handle_sayings"    
    BTN_BOT_CONFIGURATION = "btn_bot_configuration"
    BTN_HANDLE_USERS = "btn_handle_users"

    BTN_NS_ADD_TITLE = "btn_ns_add_title"
    BTN_NS_ADD_DESCRIPTION = "btn_ns_add_description"
    BTN_NS_ADD_AUTHOR = "btn_ns_add_author"
    BTN_NS_SAVE = "btn_ns_save"
    BTN_NS_DISCARD = "btn_ns_save"


    #CALLBACKS
    CB_INSERT_NEW_SAYING = "cb_insert_new_saying"
    CB_HANDLE_SAYINGS = "cb_handle_sayings"
    CB_BOT_CONFIGURATION = "cb_bot_configuration"
    CB_HANDLE_USERS = "cb_handle_users"

    CB_NS_ADD_TITLE = "cb_ns_add_title"
    CB_NS_ADD_DESCRIPTION = "cb_ns_add_description"
    CB_NS_ADD_AUTHOR = "cb_ns_add_author"
    CB_NS_SAVE = "cb_ns_save"
    CB_NS_DISCARD = "cb_ns_save"

