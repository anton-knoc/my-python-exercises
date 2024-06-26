# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для этого использовать шаблон template и подставить в него значения из строки
ospf_route. Значения из строки ospf_route надо получить с помощью Python.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""

"""
values_ospf = ospf_route.split()
metric = values_ospf[1].strip('[],')
gw = values_ospf[3].strip('[],')
time = values_ospf[4].strip('[],')
print(template.format(values_ospf[0],metric,gw,time,values_ospf[5]))
"""

ospf_route = ospf_route.replace('[','').replace(']','').replace(',','')
values_ospf = ospf_route.split()

print(template.format(values_ospf[0],values_ospf[1],values_ospf[3],values_ospf[4],values_ospf[5]))

