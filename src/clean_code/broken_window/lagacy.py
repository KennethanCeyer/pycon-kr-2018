def buzz(num, rule):
    message = ('clap' if num > 5\
        else 'buzz!') if num % rule == 0\
            else num

    print(message)


def main():
    rule = 3
    for num in range(1, 10):
        buzz(num, rule)


if __name__ == '__main__':
    main()
