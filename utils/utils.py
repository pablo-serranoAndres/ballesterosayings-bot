import os

from ui.enums.roles import Roles


def get_role(message):
    if message.from_user ==  os.getenv("ADMIN_ID"):
        return Roles.ADMIN
    else:
        return Roles.USER
