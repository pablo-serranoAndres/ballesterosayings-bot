import sqlite3
from dotenv import load_dotenv
from config import DB_CURRENT_VERSION, DB_NAME
from db.sql import *

# load_dotenv()

def check_versions_db ():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(check_table_versions_sql)
    
    if (cursor.fetchone()):
        cursor.execute(check_version_sql)
        row = cursor.fetchone()
        version = row[0]

    else :
        cursor.execute(create_versions_table_sql)
        cursor.execute(insert_version_table_sql)
        version = 0

    if(version < DB_CURRENT_VERSION):
        if(version <= 0) :
            cursor.execute(create_users_table_sql)
            cursor.execute(create_sayings_table_sql)
            # cursor.execute(insert_base_config_sql, (user_id,))
            cursor.execute(insert_current_sayings_sql)
            cursor.execute(update_version_table_sql, (DB_CURRENT_VERSION,))
            
        cursor.execute(update_version_table_sql, (DB_CURRENT_VERSION,))

    conn.commit()
    cursor.close()
    conn.close()