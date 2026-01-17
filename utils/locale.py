import json
import os

FILE_PATH = os.path.join("locales", "es.json")

with open(FILE_PATH, "r", encoding="utf-8") as file:
    LOCALE = json.load(file)