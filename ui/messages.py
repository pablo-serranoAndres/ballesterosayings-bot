
from functools import reduce

from enums.app_action import AppAction

from services.sessions import SESSIONS
from ui.icons import ICONS_MAP
from ui.markup import MARKUP_MAP
from ui.strings import STRINGS_MAP
from utils.locale import LOCALE

def deep_get(user_lang: str, keys:tuple):
    return reduce(lambda acc, key:acc[key], keys, LOCALE[user_lang])

def get_message(user_id: int, app_action: AppAction) -> str :
    user_lang = SESSIONS.get(user_id).lang
    
    return f'{
         deep_get(user_lang, ICONS_MAP[app_action])
    } {
         deep_get(user_lang, STRINGS_MAP[app_action])
    }'

def get_markup(user_id:int, app_action: AppAction) :
    markup = MARKUP_MAP.get(app_action)

    if (markup):
        markup(user_id)
    print ("keyboard_factory")