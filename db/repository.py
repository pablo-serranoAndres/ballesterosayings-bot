


import sqlite3
from models.saying import Saying
from models.user import User
from ui.enums.db_action import DBAction
from db.sql import *

def handle_db(
        action:DBAction, 
        saying: Saying = None,
        saying_id: int = None,
        session:User = None) :
    
    conn = sqlite3.connect("ballestero_sayings.db")
    cursor = conn.cursor()

    if action == DBAction.INSERT_SAYING:
        cursor.execute(insert_new_saying_sql,(saying.title, saying.description, saying.author, session.user_id ))

    elif action == DBAction.SELECT_SAYINGS:
        rows = cursor.execute(select_all_sayings_sql, (session.page_limit, session.offset,))
        sayings = rows.fetchall()
        return sayings
    
    elif action == DBAction.SELECT_SAYING_BY_ID.value:
        row = cursor.execute(select_saying_by_id_sql, (saying_id,))
        saying = row.fetchone()
        return saying
    
    elif action == DBAction.DELETE_SAYING.value:
        cursor.execute(delete_saying_by_id_sql,(saying_id,))

    elif action == DBAction.UPDATE_SAYING:
        cursor.execute(update_saying_by_id_sql,(saying.title, saying.description, saying.author,saying.id,))
        
    elif action == DBAction.COUNT_SAYINGS.value:
        rows = cursor.execute(count_sayings_sql)
        return rows

    elif action == DBAction.UPDATE_LANG_CONFIG:
        cursor.execute(update_lang_config_sql, (session.lang.strip(), session.user_id, ))

    elif action == DBAction.UPDATE_AUTORIZED:
        cursor.execute(update_autorized_sql, (session.autorized, session.user_id, ))    

    elif action == DBAction.INSERT_USER:
        cursor.execute(insert_user_sql, (session.user_id, session.username, session.menu_status.value, session.offset, session.page_limit, session.lang))
    
    elif action == DBAction.GET_USER_BY_ID:
        user = cursor.execute(get_user_by_id_sql, (session.user_id,))
    
        return user.fetchone()
    elif action == DBAction.GET_ALL_USERS:
        rows = cursor.execute(get_all_users_sql, )
        return rows.fetchall()
    

    conn.commit()
    cursor.close()
    conn.close()