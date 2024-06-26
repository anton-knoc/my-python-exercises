# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_addr = input("Enter IP address:")
ip = int(ip_addr.split('.')[0])

if ip_addr == '0.0.0.0':
    print('unassigned')
elif ip_addr == '255.255.255.255':
    print('local broadcast')
elif 1 <= ip <= 223:
    print('unicast')
elif 224 <= ip <= 239:
    print('multicast')
else:
    print('unused')

