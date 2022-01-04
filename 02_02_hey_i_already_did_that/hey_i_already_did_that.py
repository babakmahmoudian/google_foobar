def change_base(n, b):
    if n == '0':
        return '0'
    digits = ''
    while n != 0:
        digits = str(int(n % b)) + digits
        n //= b
    return digits


def get_next_id(n, b):
    n_as_list = [digit for digit in n]
    x = int(''.join(sorted(n_as_list, reverse=True)), b)
    y = int(''.join(sorted(n_as_list, reverse=False)), b)
    diff = change_base(x - y, b)
    z = '0' * (len(n) - len(diff)) + diff
    return z


def get_cycle_length(n, b):
    id_list = {}

    while True:
        n = get_next_id(n, b)
        if n not in id_list:
            id_list[n] = 1
        elif id_list[n] < 2:
            id_list[n] += 1
        else:
            break

    cycle = [key for key in id_list if id_list[key] == 2]

    return len(cycle)


def solution(n, b):
    return get_cycle_length(n, b)
