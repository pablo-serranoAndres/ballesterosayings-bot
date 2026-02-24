from enum import Enum

class FormStatus(Enum):
    # New saying
    NEW_SAYING = "new_saying"
    WAITING_TITLE = "ask_new_title"
    WAITING_DESCRIPTION = "ask_new_description"
    WAITING_AUTHOR = "ask_new_author"
    CONFIRM_CREATION = "confirm_creation"

    # Delete saying
    ASK_ID_DELETE = "delete_saying"
    SEND_SAYING_DELETE = "waiting_id_eliminate"
    CONFIRM_DELETE = "confirm_delete"
    KEEP_SAYING = "keep_saying"

    #Edit saying
    ASK_ID_UPDATE = "update_saying"
    WAITING_ID_UPDATE = "waiting_id_update"
    SEND_SAYING_UPDATE = "send_saying_update"
    EDITING_TITLE = "editing_title"
    EDITING_DESCRIPTION = "editing_description"
    EDITING_AUTHOR = "editing_author"


    # Feedback    
    DATA_SAVED = "saved_data"
    NO_DATA_FOUND = "no_data_found"
    REGISTERING_USER = "registering user"
    HANDLE_LANGS = "handling_langs"