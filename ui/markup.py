from enums.app_action import AppAction
from ui.keyboard_factory import *

MARKUP_MAP = {
    AppAction.WELCOME_MENU : general_menu,
    AppAction.INSERTING_NEW_SAYING: new_saying
}