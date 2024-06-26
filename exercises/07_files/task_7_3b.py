# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
table = []
vlan = input('Enter Vlan number:')

with open ('/home/anton_k/repos/my-python-exercises/exercises/07_files/CAM_table.txt', 'r') as f:
    for line in f:
        line_list = line.split()
        if line_list and line_list[0].isdigit() and line_list[0] == vlan:
            line_list = int(line_list[0]), line_list[1], line_list[3]
            table.append(list(line_list))
    for t in sorted(table):
        print(f'{t[0]:<8}{t[1]:<16}{t[2]:<12}')