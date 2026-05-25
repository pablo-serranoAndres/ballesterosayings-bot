from enums.app_action import AppAction


STRINGS_MAP = {

    # MENSAJES
    AppAction.WELCOME_MENU:["welcome_menu"],
    AppAction.MAIN_MENU:["main_menu"],
    AppAction.USER_NOT_AUTORIZATED : ["admin", "user_not_autorizated"],

    # BOTONES
    AppAction.BTN_INSERT_NEW_SAYING:["menu","new_saying"],
    AppAction.BTN_HANDLE_SAYINGS:["menu","handle_sayings"],
    AppAction.BTN_BOT_CONFIGURATION:["menu","configuration"],
    AppAction.BTN_HANDLE_USERS:["menu","user_admin"],

    AppAction.BTN_NSY_ADD_TITLE:["menu","configuration"],
    AppAction.BTN_NSY_ADD_DESCRIPTION:["menu","configuration"],
    AppAction.BTN_NSY_ADD_AUTHOR:["menu","configuration"],


    

}
