from enum import Enum

class Permission(Enum):
    ADMIN = 1
    USER = 2
    ANONYMOUSE = 3

def get_user_permit(code):
    if code == 'A':
        return Permission.ADMIN
    elif code == 'U':
        return Permission.USER
    else:
        return Permission.ANONYMOUSE