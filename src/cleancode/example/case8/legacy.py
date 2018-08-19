from enum import Enum

class Status(Enum):
    SUCCESS = 1
    FAIL = 2


def example():
    user = getUser()
    post = getPost(user)

    if not post:
        return Status.FAIL

    # remove post with admin
    if is_user_admin(user):
        remove_post(post.id)
        send_log(user.id)
        send_log(post.owner)
    else:
        send_error(user.id)

    return Status.SUCCESS


def is_user_admin(user):
    pass


def send_log(id):
    pass


def send_error(id):
    pass


def remove_post(id):
    pass


def getPost(user):
    # return some post
    return {
        'id': 1,
        'owner': 2,
        'title': 'hello world',
        'content': 'no content',
        'date': '2018-01-01'
    }

def getUser():
    # return some user
    return {
        'name': 'john',
        'type': 'user',
        'permit': 'user'
    }