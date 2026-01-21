from enum import Enum


class AppAction(Enum):
        # General menu
    INSERT_NEW_SAYING = "btn_insert_new_saying"
    WATCH_ALL_SAYINGS = "btn_select_all_sayings"
    DELETE_SAYING = "btn_delete_saying"
    UPDATE_SAYING = "btn_update_saying"
    CONFIG = "btn_config"

        # Go Home Indicator
    HOME_PAGE = "btn_home_page"

        # Next Previous Indicators
    NEXT_PAGE = "btn_next_page"
    PREVIOUS_PAGE = "btn_previous_page"
    #HOME_PAGE = "btn_home_page"

        # Saying Item Delete
    CONFIRM_DELETE = "btn_confirm_delete_saying"
    KEEP_SAYING = "btn_confirm_keep_saying"

        # Saying Item Edit
    EDIT_TITLE = "btn_edit_title"
    EDIT_DESCRIPTION = "btn_edit_description"
    EDIT_AUTHOR = "btn_edit_author"
    
        # Config Menu
    #CONFIG_BUTTON = "btn_config"
    LANG_CONFIG_BUTTON = "btn_lang_switch_config"
    LIMIT_CONFIG_BUTTON = "btn_query_limit_config"
    
        # Status (?)
    INTRODUCTION = "app_introduction"
    BACK_HOME = "app_back_home"
    WATCHING_SAYINGS = "watching_sayings"


    
    


