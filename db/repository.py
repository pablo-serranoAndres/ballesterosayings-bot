import sqlite3
from db.sql import *
from models.saying import Saying
from ui.enums.db_action import DBAction


def handle_db(
        action:DBAction, 
        saying: Saying = None, 
        saying_id: int = None,
        user_id: int = None,
        limit: int = None,
        offset: int = None) :
    
    conn = sqlite3.connect("ballestero_sayings.db")
    cursor = conn.cursor()

    if action == DBAction.INSERT_SAYING.value:
        cursor.execute(insert_new_saying_sql,(saying.title, saying.description, saying.author, user_id))

    elif action == DBAction.SELECT_SAYINGS:

        rows = cursor.execute(select_all_sayings_sql, (limit, offset,))
        sayings = rows.fetchall()

        return sayings
    
    elif action == DBAction.SELECT_SAYING_BY_ID.value:
        row = cursor.execute(select_saying_by_id_sql, (saying_id,))
        saying = row.fetchone()

        return saying
    
    elif action == DBAction.DELETE_SAYING.value:
        cursor.execute(delete_saying_by_id_sql,(saying_id,))

    elif action == DBAction.UPDATE_SAYING.value:
        print("")
        
    elif action == DBAction.COUNT_SAYINGS.value:
        rows = cursor.execute(count_sayings_sql)
        
        return rows

    conn.commit()
    cursor.close()
    conn.close()