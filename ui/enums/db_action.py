from enum import Enum


class DBAction(Enum):
    INSERT_SAYING = "insert_new_saying"
    SELECT_SAYINGS = "select_all_sayings"
    SELECT_SAYING_BY_ID = "select_by_id"
    DELETE_SAYING = "delete_saying"
    UPDATE_SAYING = "update_saying"
    COUNT_SAYINGS = "count_sayings"