from enums.app_action import AppAction

ICONS_MAP = {
   # MENSAJES
   AppAction.WELCOME_MENU:["icons", "hello"],
   AppAction.MAIN_MENU:["icons", "pin"],

    # CALBACKS
    AppAction.CB_NS_ADD_TITLE:["icons","new_saying"],
    AppAction.CB_NS_ADD_DESCRIPTION:["icons","new_saying"],
    AppAction.CB_NS_ADD_AUTHOR:["icons","new_saying"],

    # BOTONES
   AppAction.BTN_INSERT_NEW_SAYING:["icons","new_saying"],
   AppAction.BTN_HANDLE_SAYINGS:["icons","title"],
   AppAction.BTN_BOT_CONFIGURATION:["icons","configuration"],
   AppAction.BTN_HANDLE_USERS:["icons","author"],
   
   AppAction.BTN_NS_ADD_TITLE:["icons","title"],
   AppAction.BTN_NS_ADD_DESCRIPTION:["icons","description"],
   AppAction.BTN_NS_ADD_AUTHOR:["icons","author"],
   AppAction.BTN_NS_SAVE:["icons","success"],
   AppAction.BTN_NS_DISCARD:["icons","delete"]

}