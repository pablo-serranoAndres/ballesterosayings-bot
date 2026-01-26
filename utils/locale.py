import json
import os
from pathlib import Path
from typing import List
from db.service import update_lang
from utils.sessions import SESSIONS

LOCALE = {}

def open_locale(user_id:int) :
    user_lang = SESSIONS[user_id].lang
    
    file_path = Path("locales", f'{user_lang}.json')

    if not os.path.exists(file_path):
        file_path = Path("locales", "en.json")

    with open(file_path, "r", encoding="utf-8") as file:
        LOCALE[user_lang] = json.load(file)

def switch_locale(user_id: int, new_lang: str):
    SESSIONS[user_id].lang = new_lang
    update_lang(user_id, new_lang)
    
    open_locale(user_id)


def get_available_langs():
    available_langs: List[str] = []

    for file in Path("locales").iterdir():
        available_langs.append(file.name.split(".")[0])

    return available_langs
    


