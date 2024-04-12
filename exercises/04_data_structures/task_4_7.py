# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

mac = "AAAA:BBBB:CCCC"

#2nd attemp
result = bin(int(mac.replace(":", ""), 16)).lstrip('0b')
print(result)

#1st attemp
"""
mac1_hex = bin(int(mac[0:2], 16)).lstrip('0b')
mac2_hex = bin(int(mac[2:4], 16)).lstrip('0b')
mac3_hex = bin(int(mac[5:7], 16)).lstrip('0b')
mac4_hex = bin(int(mac[7:9], 16)).lstrip('0b')
mac5_hex = bin(int(mac[10:12], 16)).lstrip('0b')
mac6_hex = bin(int(mac[12:14], 16)).lstrip('0b')
mac2 = ''.join([mac1_hex, mac2_hex, mac3_hex, mac4_hex, mac5_hex, mac6_hex])
print(mac2)
"""
