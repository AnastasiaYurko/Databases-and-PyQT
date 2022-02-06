"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения («Узел
доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
"""

from ipaddress import ip_address
from subprocess import call
import platform


def host_ping(list_ip):
    dict_res = dict()
    for el in list_ip:
        params = f'ping -n 4 {el}' if platform.system().lower() == 'windows' else f'ping -c 4 {el}'
        result_code = call(params)
        dict_res[str(el)] = "Узел недоступен" if result_code else "Узел доступен"
    return dict_res


if __name__ == '__main__':
    ip_start = int(ip_address('192.168.1.0'))
    ip_end = int(ip_address('192.168.1.0') + 3)
    iplist = [ip_address(ip_el) for ip_el in range(ip_start, ip_end + 1)]
    print(host_ping(iplist))
