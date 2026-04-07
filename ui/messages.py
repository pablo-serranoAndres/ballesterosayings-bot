
from functools import reduce

from models.saying import Saying
from models.user import User
from enums.app_action import AppAction
from enums.form_status import AppAction
from enums.help_feedback import HelpFeedback
from services.sessions import SESSIONS
from ui.icons import ICONS_MAP
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

def build_user_auth(admin_id: int, session:User):
    user_lang = SESSIONS[admin_id].lang

    return f'{LOCALE[user_lang]["icons"]["pin"]} <b>NUEVO USUARIO</b>\n\n¿Autorizar a <b>{session.username}</b> (<u>{session.user_id}</u>) a usar el bot?'

def build_user_display(admin_id: int,session: User):
    user_lang = SESSIONS[admin_id].lang
    lines = []
    
    if (session.autorized == True) :
        lines.append(f'{LOCALE[user_lang]["icons"]["success"]} {LOCALE[user_lang]["admin"]["user"]["acepted"]}')
    elif (session.autorized == False):
        lines.append(f'{LOCALE[user_lang]["icons"]["delete"]} {LOCALE[user_lang]["admin"]["user"]["rejected"]}')

    lines.append(f'{LOCALE[user_lang]["admin"]["user"]["id"]}: *{session.user_id}*')
    lines.append(f'{LOCALE[user_lang]["admin"]["user"]["username"]}: *{session.username}*')
   
    return "\n".join(lines)

def build_saying_display (saying: Saying, form_status: AppAction, user_id:int):
    user_lang = SESSIONS[user_id].lang
    header = "" 
    footer = ""

    if (form_status == AppAction.SEND_SAYING_DELETE): 
        header = f'{LOCALE[user_lang]["icons"]["delete"]} {LOCALE[user_lang]["forms"]["delete"]["delete_confirmation"]}' 
    
    elif (form_status == AppAction.CONFIRM_CREATION):
        header = f'{LOCALE[user_lang]["icons"]["new_saying"]} {LOCALE[user_lang]["forms"]["new_saying"]["confirm_new_saying"]}' 
        # footer = f'*{LOCALE[user_lang]["forms"]["edit"]["pick_option"]}*'
    
    elif (form_status == AppAction.SEND_SAYING_UPDATE):
        header = f'{LOCALE[user_lang]["icons"]["update"]} {LOCALE[user_lang]["forms"]["edit"]["edit_confirmation"]}' 
        footer = f'*{LOCALE[user_lang]["forms"]["edit"]["pick_option"]}*'
        
    lines = []
    if (header):
        lines.append(header)
        
    lines.append(f'*{LOCALE[user_lang]["icons"]["pin"]} {LOCALE[user_lang]["saying"]["type"]}*  *#{saying.id}*\n')
    lines.append(f'{LOCALE[user_lang]["icons"]["title"]} _{LOCALE[user_lang]["saying"]["title"]}_: {saying.title}')
    lines.append(f'{LOCALE[user_lang]["icons"]["description"]} _{LOCALE[user_lang]["saying"]["description"]}_: {saying.description}')
    lines.append(f'{LOCALE[user_lang]["icons"]["author"]} _{LOCALE[user_lang]["saying"]["author"]}_: {saying.author}\n')
    
    if (footer): 
        lines.append(footer)

    text = ("\n".join(lines))
    return text

def get_help_message (user_id:int, app_location:HelpFeedback) :
    user_lang = SESSIONS[user_id].lang

    if (app_location == HelpFeedback.SAYING_PAGINATION_OPTIONS):
            return f'{LOCALE[user_lang]["icons"]["help"]} {LOCALE[user_lang]["menu"]["sayings_pagination_options"]}'
    
    elif (app_location == HelpFeedback.USERS_PAGINATION_OPTIONS):
            return f'{LOCALE[user_lang]["icons"]["help"]} {LOCALE[user_lang]["menu"]["users_pagination_options"]}'
    
    elif (app_location == HelpFeedback.CONGIGURATION_OPTIONS):
            return f'{LOCALE[user_lang]["icons"]["help"]} {LOCALE[user_lang]["feedback"]["lang_config_help"]}'
    
    elif (app_location == HelpFeedback.SAYING_TO_EDIT_CREATED):
            return f'{LOCALE[user_lang]["icons"]["help"]} {LOCALE[user_lang]["feedback"]["editing_sayings_help"]}'
    else :
        return f'{LOCALE[user_lang]["icons"]["danger"]} {LOCALE[user_lang]["feedback"]["error"]}'

def get_lang_info(user_id: int, lang:str):
    # user_lang = USER_LANG[user_id]
    user_lang = SESSIONS[user_id].lang
    return f'{LOCALE[user_lang]["icons"]["lang_flags"][lang]} {LOCALE[user_lang]["lang_config"][lang]}'

