from db.service import get_lang_config
from models.saying import Saying
from ui.enums.app_action import AppAction
from ui.enums.form_status import FormStatus
from ui.enums.help_feedback import HelpFeedback
from utils.locale import LOCALE, USER_LANG

def get_message(user_id:int, status: FormStatus | AppAction) -> str :
    # user_lang = get_lang_config(user_id)
    user_lang = USER_LANG[user_id]

    if isinstance(status, FormStatus) :
        if (status == FormStatus.NEW_SAYING):
            return LOCALE[user_lang]["forms"]["new_saying"]["new_title"]
        
        elif (status == FormStatus.WAITING_TITLE):
            return LOCALE[user_lang]["forms"]["new_saying"]["new_description"]
        
        elif (status == FormStatus.WAITING_DESCRIPTION):
            return LOCALE[user_lang]["forms"]["new_saying"]["new_author"]
        
        elif (status == FormStatus.DATA_SAVED):
            return f'{LOCALE[user_lang]["icons"]["success"]} {LOCALE[user_lang]["forms"]["feedback"]["save_saying"]}'
        
        elif (status == FormStatus.ASK_ID_DELETE):
            return f'{LOCALE[user_lang]["icons"]["delete"]} {LOCALE[user_lang]["forms"]["delete"]["ask_saying_id"]}'
        
        elif (status == FormStatus.SEND_SAYING_DELETE) : 
            return f'{LOCALE[user_lang]["icons"]["delete"]} {LOCALE[user_lang]["forms"]["delete"]["ask_saying_id"]}' 
        
        elif (status == FormStatus.CONFIRM_DELETE) : 
            return f'{LOCALE[user_lang]["icons"]["danger"]} {LOCALE[user_lang]["forms"]["delete"]["confirm_delete"]}'
        
        elif (status == FormStatus.KEEP_SAYING) :
            return f'{LOCALE[user_lang]["icons"]["success"]} {LOCALE[user_lang]["forms"]["feedback"]["save_saying"]}'
        
        elif (status == FormStatus.NO_DATA_FOUND) : 
            return f'{LOCALE[user_lang]["icons"]["attention"]} {LOCALE[user_lang]["feedback"]["no_data_found"]}'
        
        elif (status == FormStatus.NO_DATA_FOUND) : 
            return f'{LOCALE[user_lang]["icons"]["attention"]} {LOCALE[user_lang]["feedback"]["no_data_found"]}'
    
    elif isinstance(status, AppAction):
        
        if (status == AppAction.INTRODUCTION) : 
            return f'{LOCALE[user_lang]["introduction"]}'
        
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
            # return f'{LOCALE[user_lang]["icons"]["configuration"]} {LOCALE[user_lang]["menu"]["configuration_options"]}\n {LOCALE[user_lang]["icons"]["help"]} {LOCALE[user_lang]["menu"]["lang_config_help"]}\n\n {LOCALE[user_lang]["icons"]["help"]} {LOCALE[user_lang]["menu"]["limit_config_help"]}\n'
    
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
            return f'{LOCALE[user_lang]["icons"]["description"]} {LOCALE[user_lang]["edit"]["forms"]["description"]}'
        
        elif (status == AppAction.EDIT_AUTHOR) : 
            return f'{LOCALE[user_lang]["icons"]["author"]} {LOCALE[user_lang]["forms"]["edit"]["author"]}'
         
        elif (status == AppAction.LANG_CONFIG_BUTTON) : 
            return f'{LOCALE[user_lang]["icons"]["switch"]} {LOCALE[user_lang]["menu"]["lang_config"]}'
         
        elif (status == AppAction.LIMIT_CONFIG_BUTTON) : 
            return f'{LOCALE[user_lang]["icons"]["limit"]} {LOCALE[user_lang]["menu"]["limit_config"]}'
        
        elif (status == AppAction.BACK_HOME) : 
            return f'{LOCALE[user_lang]["new_action"]}'

        # elif (status == AppAction.WATCHING_SAYINGS) : 
        #     return
        
    else :
        return f'{LOCALE[user_lang]["feedback"]["error"]}'

def build_saying_display (saying: Saying, form_status: FormStatus, user_id:int):
    user_lang = USER_LANG[user_id]
    header = ""

    if (form_status == FormStatus.SEND_SAYING_DELETE): 
        header = LOCALE[user_lang]["forms"]["delete"]["delete_confirmation"]

    return (
        f'''
{header}
*{LOCALE[user_lang]["icons"]["pin"]} {LOCALE[user_lang]["saying"]["type"]}  #{saying.id}*
{LOCALE[user_lang]["icons"]["title"]} _{LOCALE[user_lang]["saying"]["title"]}_: {saying.title}
{LOCALE[user_lang]["icons"]["description"]} _{LOCALE[user_lang]["saying"]["description"]}_: {saying.description}
{LOCALE[user_lang]["icons"]["author"]} _{LOCALE[user_lang]["saying"]["author"]}_: {saying.author}
    '''
    )

def get_help_message (user_id:int, app_location:HelpFeedback) :
    user_lang = USER_LANG[user_id]

    if (app_location == HelpFeedback.PAGINATION_OPTIONS):
            return f'{LOCALE[user_lang]["icons"]["help"]} {LOCALE[user_lang]["menu"]["pagination_options"]}'
    else :
        return f'{LOCALE[user_lang]["icons"]["danger"]} {LOCALE[user_lang]["feedback"]["error"]}'
