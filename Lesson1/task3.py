"""
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном случае
результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate).
Таблица должна состоять из двух колонок и выглядеть примерно так:
Reachable
10.0.0.1
10.0.0.2

Unreachable
10.0.0.3
10.0.0.4
"""

from Lesson1.task2 import host_range_ping
from tabulate import tabulate


def rows_ongo(details:tuple):
    res = []
    rows = len(details[0]) if len(details[0]) > len(details[1]) else len(details[1])
    for _ in range(rows):
        try:
            left_col = details[0][_]
        except IndexError:
            left_col = ''
        try:
            right_col = details[1][_]
        except IndexError:
            right_col = ''
        res.append((left_col, right_col))
    return res


def host_range_ping_tab(ip_range):
    reachable_list = []
    unreachable_list = []
    ping_result = host_range_ping(ip_range)
    for a, n in ping_result.items():
        if n == "Узел недоступен":
            unreachable_list.append(a)
        else:
            reachable_list.append(a)
    return reachable_list, unreachable_list


if __name__ == "__main__":
    ping_result = host_range_ping_tab("192.168.1.0-4")
    ROWS = rows_ongo(ping_result)
    COLUMNS = ['Reachable', 'Unreachable']
    print(tabulate(ROWS, headers=COLUMNS, tablefmt="grid"))