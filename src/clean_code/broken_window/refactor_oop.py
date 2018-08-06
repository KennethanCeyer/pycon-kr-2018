_BUZZ_MESSAGE_ = 'buzz!'
_CLAP_MESSAGE_ = 'clap'
_RULE_ = 3
_THRESHOLD_ = 5

class Buzz():
    def __init__(self):
        self.threshold = _THRESHOLD_
        self.buzz_message = _BUZZ_MESSAGE_
        self.clap_message = _CLAP_MESSAGE_
        self.rule = _RULE_

    def get_message(self, num):
        if (num % self.rule != 0):
            return num
        if (num > self.threshold):
            return self.clap_message
        return self.buzz_message

    def print(self, num,):
        print(self.get_message(num))


def main():
    buzz = Buzz()
    for num in range(1, 10):
        buzz.print(num)


if __name__ == '__main__':
    main()
