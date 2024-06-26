# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]


#solution 1 - hardcode of ignore
"""
from sys import argv #enter arg1 via CLI

path = '/home/anton_k/repos/my-python-exercises/exercises/07_files/' + argv[1]

with open(path, 'r') as f:
    for line in f:
        if line.startswith('!') or line.count(ignore[0]) >= 1 or line.count(ignore[1]) >= 1 or line.count(ignore[2]) >= 1 :
            continue
        else:
            print(line.rstrip())
"""

#solution 2
from sys import argv #enter arg1 via CLI

path = '/home/anton_k/repos/my-python-exercises/exercises/07_files/' + argv[1]

with open(path, 'r') as f:
    for line in f:
        check_lintersection = line.split()
        check_lintersection = set(check_lintersection) & set(ignore)
        if line.startswith('!') or check_lintersection:
            continue
        else:
            print(line.rstrip())
