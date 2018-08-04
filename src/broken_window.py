def buzz(num):
    message = ('clap' if num > 5\
        else 'buzz!') if num % 3 == 0\
            else num

    print(message)


def main():
    for num in range(1, 10):
        buzz(num)


if __name__ == '__main__':
    main()
