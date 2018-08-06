from enum import Enum

class Status(Enum):
    SUCCESS = 1
    FAIL = 2


def example():
    user = get_user()
    if user != None and user.type == 'anonymous':
        post = get_post(user)
        if post != None and post.title != None:
            comment = get_comment(post)
            status = do_with_comment(comment)
            if status == False:
                return Status.FAIL
            else:
                return Status.SUCCESS
        return Status.FAIL
    return Status.FAIL


def do_with_comment(comment):
    # do something complex job about comment
    pass


def get_comment(post):
    # return some comment
    return {
        'id': 1,
        'content': 'hello world',
        'user': 4,
        'date': '2018-01-01'
    }


def get_post(user):
    # return some post
    return {
        'id': 1,
        'title': 'hello world',
        'content': 'no content',
        'date': '2018-01-01'
    }


def get_user():
    # return some user
    return {
        'name': 'john',
        'type': 'user',
        'permit': 'user'
    }