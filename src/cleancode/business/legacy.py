def get_users():
    return [
        { 'id': 1, 'name': 'user1', 'permission': 'admin' },
        { 'id': 2, 'name': 'user2', 'permission': 'user' },
        { 'id': 3, 'name': 'user3', 'permission': 'anonymous' },
        { 'id': 4, 'name': 'user4', 'permission': 'user' },
        { 'id': 5, 'name': 'user5', 'permission': 'user' }
    ];


def main():
    print(len(get_users()))


if __name__ == '__main__':
    main()