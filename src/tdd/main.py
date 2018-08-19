def _filter_odd(num):
    return num % 2 == 1


def _get_odd_len(num_list):
    return len(list(filter(_filter_odd, num_list)))


def calc(num_list):
    return _get_odd_len(num_list) * 5
