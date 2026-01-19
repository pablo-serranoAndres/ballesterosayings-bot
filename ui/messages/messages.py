from models.saying import Saying
from ui.enums.form_status import FormStatus
from utils.locale import LOCALE

MESSAGES = {
    FormStatus.NEW_SAYING: LOCALE["forms"]["new_saying"]["new_title"],
    FormStatus.WAITING_TITLE: LOCALE["forms"]["new_saying"]["new_description"],
    FormStatus.WAITING_DESCRIPTION: LOCALE["forms"]["new_saying"]["new_author"],
    FormStatus.DATA_SAVED: f'{LOCALE["icons"]["success"]} {LOCALE["forms"]["feedback"]["save_saying"]}',
    FormStatus.ASK_ID_DELETE: f"{LOCALE["icons"]["delete"]} {LOCALE["forms"]["delete"]["ask_saying_id"]}",
    FormStatus.SEND_SAYING_DELETE: f"{LOCALE["icons"]["delete"]} {LOCALE["forms"]["delete"]["ask_saying_id"]}",
    FormStatus.CONFIRM_DELETE: f'{LOCALE["icons"]["danger"]} {LOCALE["forms"]["delete"]["confirm_delete"]}',
    FormStatus.KEEP_SAYING: f'{LOCALE["icons"]["success"]} {LOCALE["forms"]["feedback"]["save_saying"]}',
    FormStatus.NO_DATA_FOUND: f'{LOCALE["icons"]["attention"]} {LOCALE["forms"]["feedback"]["no_data_found"]}' 
}



def build_saying_display (saying: Saying, form_status: FormStatus):
    header = ""

    if (form_status == FormStatus.SEND_SAYING_DELETE): 
        header = LOCALE["forms"]["delete"]["delete_confirmation"]

 
    return (
        f'''
    {header}
    {LOCALE["icons"]["pin"]} {LOCALE["saying"]["type"]}  #{saying.id}
    {LOCALE["icons"]["title"]} {LOCALE["saying"]["title"]} : {saying.title}
    {LOCALE["icons"]["description"]} {LOCALE["saying"]["description"]} : {saying.description}
    {LOCALE["icons"]["author"]} {LOCALE["saying"]["author"]} : {saying.author}
    '''
    )
    
  

       
    