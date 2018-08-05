_BUZZ_MESSAGE_ = 'buzz!'
_CLAP_MESSAGE_ = 'clap'
_RULE_ = 3
_THRESHOLD_ = 5

def get_buzz_message(num, rule):
    if (num % rule != 0):
        return num
    if (num > _THRESHOLD_):
        return _CLAP_MESSAGE_
    return _BUZZ_MESSAGE_


def buzz(num, rule):
    print(get_buzz_message(num, rule))


def main():
    rule = _RULE_
    for num in range(1, 10):
        buzz(num, rule)


if __name__ == '__main__':
    main()
