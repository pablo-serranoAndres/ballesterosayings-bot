import os
from typing import Optional
from ui.enums.form_status import FormStatus


class User:
    def __init__(
            self, 
            user_id:int, 
            first_name:str, 
            menu_status: Optional[FormStatus] = None, 
            lang:str = "es", 
            last_name:str = "", 
            offset:int = 0,  
            page_limit:int = 10):
        
        
        self.user_id = user_id
        self.username = f'{first_name} {last_name}'.strip()
        self.menu_status = menu_status
        self.offset = offset
        self.page_limit = page_limit
        self.lang = lang
        self.autorized = False