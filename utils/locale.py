import json
import os
from pathlib import Path
from typing import List
from db.service import get_lang_config, save_new_lang

LOCALE = {}
USER_LANG = {}

def open_locale(user_id:int) : 
    USER_LANG[user_id] = get_lang_config(user_id) or "en"

    user_lang = USER_LANG[user_id]
    
    file_path = Path("locales", f'{user_lang}.json')

    if not os.path.exists(file_path):
        file_path = Path("locales", "en.json")

    with open(file_path, "r", encoding="utf-8") as file:
        LOCALE[user_lang] = json.load(file)

def switch_locale(user_id: int, new_lang: str):
    save_new_lang(user_id, new_lang)
    USER_LANG[user_id] = new_lang
    
    open_locale(user_id)


def get_available_langs(user_id:int):
    available_langs: List[str] = []

    for file in Path("locales").iterdir():
        available_langs.append(file.name.split(".")[0])

    return available_langs
    


