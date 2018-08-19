import requests
import re

_URL_ = 'https://pycon.kr'


def sum(a, b):
    res = requests.get(_URL_)
    year = int(re.findall(r'\d+', res.url)[0])
    if year == 2018:
        return a + b
    return -1


if __name__ == '__main__':
    sum()
