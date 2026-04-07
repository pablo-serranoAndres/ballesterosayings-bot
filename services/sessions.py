

from db.service import get_user_by_id, insert_new_user
from enums.app_action import AppAction
from models.user import User


SESSIONS: dict[int, User] = {}

def load_session_fromRAM (user_id: int):
    return SESSIONS.get(user_id)

def load_session_fromDB (user_id: int):
    user = get_user_by_id(user_id)
    if (user is not None):
        return user
    print("load_session")

def create_session (message):
    new_user =  User (
            user_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            lang="es",
            menu_status=AppAction.REGISTERING_USER,
            page_limit=10)
    
    SESSIONS[message.from_user.id] = new_user
    insert_new_user(new_user)

    return new_user

def check_auth(user_id: int):    
    print("TODO: check_auth")
    autorizated = True
    return autorizated