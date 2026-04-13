from enums.app_action import AppAction


STRINGS_MAP = {
    # MENSAJES
    AppAction.WELCOME_MENU:["welcome_menu"],
    AppAction.MAIN_MENU:["main_menu"],

    # CALBACKS
    AppAction.CB_NS_ADD_TITLE:["form","actions", "add_title"],
    AppAction.CB_NS_ADD_DESCRIPTION:["form","actions", "add_description"],
    AppAction.CB_NS_ADD_AUTHOR:["form","actions", "add_author"],

    # BOTONES
    AppAction.BTN_INSERT_NEW_SAYING:["menu","new_saying"],
    AppAction.BTN_HANDLE_SAYINGS:["menu","handle_sayings"],
    AppAction.BTN_BOT_CONFIGURATION:["menu","configuration"],
    AppAction.BTN_HANDLE_USERS:["menu","user_admin"],
    
    AppAction.BTN_NS_ADD_TITLE:["form","new_saying","options","add_title"],
    AppAction.BTN_NS_ADD_DESCRIPTION:["form","new_saying","options","add_description"],
    AppAction.BTN_NS_ADD_AUTHOR:["form","new_saying","options","add_author"],
    AppAction.BTN_NS_SAVE:["form","new_saying","options","save_saying"],
    AppAction.BTN_NS_DISCARD:["form","new_saying","options","delete_saying"],

}
