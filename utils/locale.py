import json
import os
from db.service import get_lang_config

LOCALE = {}
USER_LANG = {}

def open_locale(user_id:int) : 
    USER_LANG[user_id] = get_lang_config(user_id) or "es"
    user_lang = USER_LANG[user_id]
    
    FILE_PATH = os.path.join("locales", f'{USER_LANG[user_id]}.json')

    if not os.path.exists(FILE_PATH):
        FILE_PATH = os.path.join("locales", "en.json")

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        LOCALE[user_lang] = json.load(file)


