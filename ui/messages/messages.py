
from models.saying import Saying
from models.user import User
from ui.enums.app_action import AppAction
from ui.enums.form_status import FormStatus
from ui.enums.help_feedback import HelpFeedback
from utils.locale import LOCALE
from utils.sessions import SESSIONS

def get_message(user_id:int, status: FormStatus | AppAction) -> str :
    user_lang = SESSIONS.get(user_id).lang
    

    if isinstance(status, FormStatus) :
        if (status == FormStatus.NEW_SAYING):
            return f'{LOCALE[user_lang]["icons"]["new_saying"]} {LOCALE[user_lang]["forms"]["new_saying"]["new_title"]}'
        
        elif (status == FormStatus.WAITING_TITLE):
            return LOCALE[user_lang]["forms"]["new_saying"]["new_description"]
        
        elif (status == FormStatus.WAITING_DESCRIPTION):
            return LOCALE[user_lang]["forms"]["new_saying"]["new_author"]
        
        elif (status == FormStatus.DATA_SAVED):
            return f'{LOCALE[user_lang]["icons"]["success"]} {LOCALE[user_lang]["feedback"]["save_saying"]}'
        
        elif (status == FormStatus.ASK_ID_DELETE):
            return f'{LOCALE[user_lang]["icons"]["delete"]} {LOCALE[user_lang]["forms"]["delete"]["ask_saying_id"]}'
        
        elif (status == FormStatus.SEND_SAYING_DELETE) : 
            return f'{LOCALE[user_lang]["icons"]["delete"]} {LOCALE[user_lang]["forms"]["delete"]["ask_saying_id"]}' 
        
        elif (status == FormStatus.CONFIRM_DELETE) : 
            return f'{LOCALE[user_lang]["icons"]["danger"]} {LOCALE[user_lang]["forms"]["delete"]["confirm_delete"]}'
        
        elif (status == FormStatus.KEEP_SAYING) :
            return f'{LOCALE[user_lang]["icons"]["success"]} {LOCALE[user_lang]["forms"]["delete"]["no_confirm_delete"]}'
        
        elif (status == FormStatus.WAITING_ID_UPDATE) :
            return f'{LOCALE[user_lang]["icons"]["title"]} {LOCALE[user_lang]["forms"]["edit"]["ask_saying_id"]}'
        
        elif (status == FormStatus.NO_DATA_FOUND) : 
            return f'{LOCALE[user_lang]["icons"]["attention"]} {LOCALE[user_lang]["feedback"]["no_data_found"]}'
        
        elif (status == FormStatus.NO_DATA_FOUND) : 
            return f'{LOCALE[user_lang]["icons"]["attention"]} {LOCALE[user_lang]["feedback"]["no_data_found"]}'
        
        elif (status == FormStatus.HANDLE_LANGS) : 
            return f'{LOCALE[user_lang]["icons"]["switch"]} {LOCALE[user_lang]["forms"]["config"]["lang"]["title"]}'
        
        elif (status == FormStatus.EDITING_TITLE) : 
            return f'{LOCALE[user_lang]["icons"]["update"]} {LOCALE[user_lang]["forms"]["edit"]["editing_title"]}'
        
        elif (status == FormStatus.EDITING_DESCRIPTION) : 
            return f'{LOCALE[user_lang]["icons"]["update"]} {LOCALE[user_lang]["forms"]["edit"]["editing_description"]}'
        
        elif (status == FormStatus.EDITING_AUTHOR) : 
            return f'{LOCALE[user_lang]["icons"]["update"]} {LOCALE[user_lang]["forms"]["edit"]["editing_author"]}'
    
    elif isinstance(status, AppAction):
        
        if (status == AppAction.INTRODUCTION) : 
            return f'{LOCALE[user_lang]["icons"]["hello"]}{LOCALE[user_lang]["introduction"]}'
        
    # general_menu()
        elif (status == AppAction.INSERT_NEW_SAYING) :
            return f'{LOCALE[user_lang]["icons"]["new_saying"]} {LOCALE[user_lang]["menu"]["new_saying"]}'
        elif (status == AppAction.WATCH_ALL_SAYINGS) :
            return f'{LOCALE[user_lang]["icons"]["select_all_sayings"]} {LOCALE[user_lang]["menu"]["select_all_sayings"]}'
        
        elif (status == AppAction.DELETE_SAYING) : 
            return f'{LOCALE[user_lang]["icons"]["delete"]} {LOCALE[user_lang]["menu"]["delete_saying"]}'
    
        elif (status == AppAction.UPDATE_SAYING) : 
            return f'{LOCALE[user_lang]["icons"]["update"]} {LOCALE[user_lang]["menu"]["update_saying"]}'
    
        elif (status == AppAction.CONFIG) : 
            return f'{LOCALE[user_lang]["icons"]["configuration"]} {LOCALE[user_lang]["menu"]["configuration"]}'
        
        elif (status == AppAction.CONFIG_MENU) : 
            return f'{LOCALE[user_lang]["icons"]["configuration"]} {LOCALE[user_lang]["menu"]["configuration_options"]} \n\n {get_help_message(user_id, HelpFeedback.CONGIGURATION_OPTIONS)}'
    
    # go_home_indicator()
        elif (status == AppAction.HOME_PAGE) : 
            return f'{LOCALE[user_lang]["icons"]["home"]} {LOCALE[user_lang]["menu"]["home"]}'
        

    # next_previous_indicators()
        elif (status == AppAction.NEXT_PAGE) : 
            return f'{LOCALE[user_lang]["icons"]["next"]} {LOCALE[user_lang]["menu"]["next_page"]}'
        
        elif (status == AppAction.PREVIOUS_PAGE) : 
            return f'{LOCALE[user_lang]["icons"]["previous"]} {LOCALE[user_lang]["menu"]["previous_page"]}'
    
    
    # saying_item_delete()
        elif (status == AppAction.KEEP_SAYING) : 
            return f'{LOCALE[user_lang]["icons"]["success"]} {LOCALE[user_lang]["forms"]["delete"]["keep_saying"]}'
        
        elif (status == AppAction.CONFIRM_DELETE) : 
            return f'{LOCALE[user_lang]["icons"]["delete"]} {LOCALE[user_lang]["forms"]["delete"]["delete_saying"]}'
        

    # saying_item_edit()
        
        elif (status == AppAction.EDIT_TITLE) : 
            return f'{LOCALE[user_lang]["icons"]["title"]} {LOCALE[user_lang]["forms"]["edit"]["title"]}'
        
        elif (status == AppAction.EDIT_DESCRIPTION) : 
            return f'{LOCALE[user_lang]["icons"]["description"]} {LOCALE[user_lang]["forms"]["edit"]["description"]}'
        
        elif (status == AppAction.EDIT_AUTHOR) : 
            return f'{LOCALE[user_lang]["icons"]["author"]} {LOCALE[user_lang]["forms"]["edit"]["author"]}'
        
        elif (status == AppAction.NOT_SAVE) : 
            return f'{LOCALE[user_lang]["icons"]["danger"]} {LOCALE[user_lang]["forms"]["edit"]["not_save"]}'
        
        elif (status == AppAction.SAVE_CHANGES) : 
            return f'{LOCALE[user_lang]["icons"]["success"]} {LOCALE[user_lang]["forms"]["edit"]["save_changes"]}'
         
        elif (status == AppAction.LANG_CONFIG_BUTTON) : 
            return f'{LOCALE[user_lang]["icons"]["switch"]} {LOCALE[user_lang]["menu"]["lang_config"]}'

        elif (status == AppAction.LIMIT_CONFIG_BUTTON) : 
            return f'{LOCALE[user_lang]["icons"]["limit"]} {LOCALE[user_lang]["menu"]["limit_config"]}'
        
        elif (status == AppAction.BACK_HOME) : 
            return f'{LOCALE[user_lang]["new_action"]}'
        
        elif (status == AppAction.APP_ERROR) : 
            return f'{LOCALE[user_lang]["icons"]["attention"]} {LOCALE[user_lang]["feedback"]["app_error"]}{LOCALE[user_lang]["new_action"]}'
        
        elif (status == AppAction.NOT_PERMITED) : 
            return f'{LOCALE[user_lang]["icons"]["danger"]} {LOCALE[user_lang]["feedback"]["not_permitted"]}{LOCALE[user_lang]["new_action"]}' 

        elif (status == AppAction.ACEPT_USER) : 
            return f'{LOCALE[user_lang]["icons"]["success"]}{LOCALE[user_lang]["admin"]["acept_user"]}'
        
        elif (status == AppAction.REJECT_USER) : 
            return f'{LOCALE[user_lang]["icons"]["delete"]} {LOCALE[user_lang]["admin"]["reject_user"]}'

        elif (status == AppAction.WAITING_AUTH_USER) : 
            return f'{LOCALE[user_lang]["icons"]["limit"]}{LOCALE[user_lang]["icons"]["author"]} {LOCALE[user_lang]["feedback"]["waiting_auth"]}'
        
        elif (status == AppAction.NEW_USER_ACEPTED) : 
            return f'{LOCALE[user_lang]["icons"]["success"]}{LOCALE[user_lang]["admin"]["new_user_acepted"]}'
        
        elif (status == AppAction.NEW_USER_REJECTED) : 
            return f'{LOCALE[user_lang]["icons"]["danger"]}{LOCALE[user_lang]["admin"]["new_user_rejected"]}'
        
        elif (status == AppAction.USER_ADMIN) : 
            return f'{LOCALE[user_lang]["icons"]["author"]}{LOCALE[user_lang]["menu"]["user_admin"]}'
        
    else :
        return f'{LOCALE[user_lang]["feedback"]["app_error"]}'

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


def build_saying_display (saying: Saying, form_status: FormStatus, user_id:int):
    user_lang = SESSIONS[user_id].lang
    header = "" 
    footer = ""

    if (form_status == FormStatus.SEND_SAYING_DELETE): 
        header = f'{LOCALE[user_lang]["icons"]["delete"]} {LOCALE[user_lang]["forms"]["delete"]["delete_confirmation"]}' 
    
    elif (form_status == FormStatus.SEND_SAYING_UPDATE):
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
    
    return "\n".join(lines)

def get_help_message (user_id:int, app_location:HelpFeedback) :
    user_lang = SESSIONS[user_id].lang

    if (app_location == HelpFeedback.SAYING_PAGINATION_OPTIONS):
            return f'{LOCALE[user_lang]["icons"]["help"]} {LOCALE[user_lang]["menu"]["sayings_pagination_options"]}'
    
    elif (app_location == HelpFeedback.USERS_PAGINATION_OPTIONS):
            return f'{LOCALE[user_lang]["icons"]["help"]} {LOCALE[user_lang]["menu"]["users_pagination_options"]}'
    
    elif (app_location == HelpFeedback.CONGIGURATION_OPTIONS):
            return f'{LOCALE[user_lang]["icons"]["help"]} {LOCALE[user_lang]["menu"]["lang_config_help"]}'
    else :
        return f'{LOCALE[user_lang]["icons"]["danger"]} {LOCALE[user_lang]["feedback"]["error"]}'

def get_lang_info(user_id: int, lang:str):
    # user_lang = USER_LANG[user_id]
    user_lang = SESSIONS[user_id].lang
    return f'{LOCALE[user_lang]["icons"]["lang_flags"][lang]} {LOCALE[user_lang]["lang_config"][lang]}'

