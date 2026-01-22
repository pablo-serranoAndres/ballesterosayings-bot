import sqlite3
from db.sql import *
from models.saying import Saying
from ui.enums.db_action import DBAction


def handle_db(
        action:DBAction, 
        saying: Saying = None, 
        saying_id: int = None,
        user_id: int = None,
        page_limit: int = None,
        config_id: str = None, 
        config_value: str = None,
        offset: int = None,
        new_lang:str = None) :
    
    conn = sqlite3.connect("ballestero_sayings.db")
    cursor = conn.cursor()

    if action == DBAction.INSERT_SAYING.value:
        cursor.execute(insert_new_saying_sql,(saying.title, saying.description, saying.author, user_id))

    elif action == DBAction.SELECT_SAYINGS:
        
        rows = cursor.execute(select_all_sayings_sql, (page_limit, offset,))
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
    
    elif action == DBAction.GET_LANG_CONFIG:
        rows = cursor.execute(get_lang_config_sql, (user_id,))
        
        return rows
    
    elif action == DBAction.UPDATE_LANG_CONFIG:
        
        cursor.execute(update_lang_config_sql, (new_lang.strip(), user_id,))


    conn.commit()
    cursor.close()
    conn.close()