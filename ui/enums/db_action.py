from enum import Enum


class DBAction(Enum):
    INSERT_SAYING = "insert_new_saying"
    SELECT_SAYINGS = "select_all_sayings"
    SELECT_SAYING_BY_ID = "select_by_id"
    DELETE_SAYING = "delete_saying"
    UPDATE_SAYING = "update_saying"
    COUNT_SAYINGS = "count_sayings"
    
    UPDATE_CONFIG = "update_config"
    GET_CONFIG = "get_config"
    GET_LANG_CONFIG = "get_lang_config"
    UPDATE_LANG_CONFIG = "update_lang_config"
    INSERT_NEW_LANG = "insert_lang"

    INSERT_USER = "insert_user"
    GET_ALL_USERS = "get_all_users"
    UPDATE_AUTORIZED = "update_autorized"
    GET_USER_BY_ID = "get_user"
    