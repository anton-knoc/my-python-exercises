# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
#solution 1

route_template =  """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""

with open('/home/anton_k/repos/my-python-exercises/exercises/07_files/ospf.txt', 'r') as f:
    for l in f:
        l_list = l.replace('[', '').replace(']', '').replace(',', '')
        l_list = l_list.split()
        print(route_template.format(l_list[1], l_list[2], l_list[4], l_list[5], l_list[6]))