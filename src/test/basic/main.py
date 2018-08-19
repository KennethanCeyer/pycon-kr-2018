__VERSION__ = '0.0.1'


def sum(a, b):
    return a + b


def get_version():
    return __VERSION__


if __name__ == '__main__':
    sum_num = sum(1, 2) # 1 + 2 = 3
    version = get_version() # 0.0.1

    print('sum', sum_num)
    print('version', version)
