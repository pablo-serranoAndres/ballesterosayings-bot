from enum import Enum


class AppAction(Enum):
    # New saying
    INSERT_NEW_SAYING = "btn_insert_new_saying"
    WATCH_ALL_SAYINGS = "btn_select_all_sayings"
    DELETE_SAYING = "btn_delete_saying"
    
    CONFIRM_DELETE = "btn_confirm_delete_saying"
    KEEP_SAYING = "btn_confirm_keep_saying"

    # Edit saying
    SEND_SAYING_EDIT = "btn_update_saying"

    # Watch sayings
    HOME_BUTTON = "btn_home_page"
    WATCHING_SAYINGS = "watching_sayings"
    NEXT_PAGE_BUTTON = "btn_next_page"
    PREVIOUS_PAGE_BUTTON = "btn_previous_page"
