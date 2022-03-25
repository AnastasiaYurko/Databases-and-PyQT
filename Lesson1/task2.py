"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только последний
октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
"""

from Lesson1.task1 import host_ping
from ipaddress import ip_address


def host_range_ping(ip_range:str):
    ip_start, last_val = tuple(ip_range.split("-"))
    address_bytes = [int(x) for x in ip_start.split('.')]
    ip_end = (
        address_bytes[0] * (256 ** 3) +
        address_bytes[1] * (256 ** 2) +
        address_bytes[2] * (256 ** 1) +
        int(last_val)
    )
    ip_start = int(ip_address(ip_start))
    iplist = [ip_address(ip_el) for ip_el in range(ip_start, ip_end + 1)]

    return host_ping(iplist)


if __name__ == "__main__":
    ip_range = "192.168.1.0-7"
    res = host_range_ping(ip_range)
    print(res)