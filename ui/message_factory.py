from typing import Literal
from models.saying import Saying
from utils import deep_get

def display_saying(
        user_lang:str,
        saying:Saying, 
        variant:Literal["NEW", "EDIT", "DELETE"]) -> str:
    title = ""
    text = ""

    if (variant == "NEW"):
        title = f'{deep_get(user_lang, ["icons", "pin"])} {deep_get(user_lang, ["menu", "new_saying"])}'
                
    elif (variant == "EDIT"):
        title = f'{deep_get(user_lang, ["icons", "pin"])} {deep_get(user_lang, ["menu", "new_saying"])}'
 
    text = f'{deep_get(user_lang, ["saying", "title"])}: {saying.title}\n\n{deep_get(user_lang,["saying", "description"])}: {saying.description}\n\n{deep_get(user_lang,["saying", "author"])}: {saying.author}'
    return f'{title}{text}'