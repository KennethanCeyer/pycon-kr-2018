import requests
import re

_URL_ = 'https://pycon.kr'


def _get_redirect(url):
    return requests.get(url)


def _get_year(get_redirect):
    return int(re.findall(r'\d+', get_redirect(_URL_).url)[0])


def sum(get_year, get_redirect, a, b):
    year = get_year(get_redirect)
    return a + b if year == 2018 else -1


if __name__ == '__main__':
    print(sum(_get_year, _get_redirect, 1, 2))
