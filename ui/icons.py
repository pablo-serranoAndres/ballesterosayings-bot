from enums.app_action import AppAction

ICONS_MAP = {
   # MENSAJES
   AppAction.WELCOME_MENU:["icons", "hello"],
   AppAction.MAIN_MENU:["icons", "pin"],
   AppAction.USER_NOT_AUTORIZATED:["icons", "pin"],

    # BOTONES
   AppAction.BTN_INSERT_NEW_SAYING:["icons","new_saying"],
   AppAction.BTN_HANDLE_SAYINGS:["icons","title"],
   AppAction.BTN_BOT_CONFIGURATION:["icons","configuration"],
   AppAction.BTN_HANDLE_USERS:["icons","author"],
   
   AppAction.BTN_NSY_ADD_TITLE:["icons","new_saying"],
   AppAction.BTN_NSY_ADD_DESCRIPTION:["icons","description"],
   AppAction.BTN_NSY_ADD_AUTHOR:["icons","author"]

}