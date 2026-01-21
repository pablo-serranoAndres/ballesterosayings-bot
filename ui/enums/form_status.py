from enum import Enum

class FormStatus(Enum):
    # New saying
    NEW_SAYING = "new_saying"
    WAITING_TITLE = "ask_new_title"
    WAITING_DESCRIPTION = "ask_new_description"
    WAITING_AUTHOR = "ask_new_author"

    # Delete saying
    ASK_ID_DELETE = "delete_saying"
    SEND_SAYING_DELETE = "waiting_id_eliminate"
    CONFIRM_DELETE = "confirm_delete"
    KEEP_SAYING = "keep_saying"

    # Feedback    
    DATA_SAVED = "saved_data"
    NO_DATA_FOUND = "no_data_found"
