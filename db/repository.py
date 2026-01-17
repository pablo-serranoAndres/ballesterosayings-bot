import sqlite3
from enum import Enum
from db.sql import *
from models.saying import Saying

class Action(Enum):
    INSERT_SAYING = "insert_new_saying"
    SELECT_SAYINGS = "select_all_sayings"
    SELECT_SAYING_BY_ID = "select_by_id"
    DELETE_SAYING = "delete_saying"
    UPDATE_SAYING = "update_saying"
    COUNT_SAYINGS = "count_sayings"


def handle_db(
        action:Action, 
        saying: Saying = None, 
        saying_id: int = None,
        user_id: int = None,
        limit: int = None,
        offset: int = None) :
    conn = sqlite3.connect("ballestero_sayings.db")
    cursor = conn.cursor()

    if action == Action.INSERT_SAYING.value:
        cursor.execute(insert_new_saying_sql,(saying.title, saying.description, saying.author, user_id))

    elif action == Action.SELECT_SAYINGS.value:
        rows = cursor.execute(select_all_sayings_sql, (limit, offset,))
        sayings = rows.fetchall()

        return sayings
    elif action == Action.SELECT_SAYING_BY_ID.value:
        row = cursor.execute(select_saying_by_id_sql, (saying_id,))
        saying = row.fetchone()

        return saying
    
    elif action == Action.DELETE_SAYING.value:
        cursor.execute(delete_saying_by_id_sql,(saying_id,))

    elif action == Action.UPDATE_SAYING.value:
        print("")
        
    elif action == Action.COUNT_SAYINGS.value:
        rows = cursor.execute(count_sayings_sql)
        
        return rows

    conn.commit()
    cursor.close()
    conn.close()