from enum import Enum

class Permission(Enum):
    ADMIN = 1
    USER = 2
    ANONYMOUSE = 3

def get_user_permit(code):
    permissions = {
        'A': Permission.ADMIN,
        'U': Permission.USER,
        '_': Permission.ANONYMOUSE
    }

    return permissions.get(code, permissions['_'])
