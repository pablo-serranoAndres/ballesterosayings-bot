from enums.app_action import AppAction


STRINGS_MAP = {
    # MENSAJES
    AppAction.WELCOME_MENU:["welcome_menu"],
    AppAction.MAIN_MENU:["main_menu"],

    # BOTONES
    AppAction.BTN_INSERT_NEW_SAYING:["menu","new_saying"],
    AppAction.BTN_HANDLE_SAYINGS:["menu","handle_sayings"],
    AppAction.BTN_BOT_CONFIGURATION:["menu","configuration"],
    AppAction.BTN_HANDLE_USERS:["menu","user_admin"]

}
