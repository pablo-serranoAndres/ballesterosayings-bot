
from enums.app_action import AppAction
from models.saying import Saying
from models.user import User
from ui.icons import ICONS_MAP
from ui.markup import MARKUP_MAP
from ui.strings import STRINGS_MAP
from utils import deep_get

def get_text(user_lang: str, app_action: AppAction) -> str :
    # user_lang = SESSIONS.get(user_id).lang
    
    return f'{
         deep_get(user_lang, ICONS_MAP[app_action])
    } {
         deep_get(user_lang, STRINGS_MAP[app_action])
    }'

def get_markup(user_id: int, app_action:AppAction):
    markup = MARKUP_MAP.get(app_action) or None
    return markup(user_id)


