# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

#solution
from sys import argv #enter arg1 via CLI

path = '/home/anton_k/repos/my-python-exercises/exercises/07_files/' + argv[1]
new_path = argv[2]

with open(path, 'r') as src, open (new_path, 'w') as dst :
    for line in src:
        check_lintersection = line.split()
        check_lintersection = set(check_lintersection) & set(ignore)
        if line.startswith('!') or check_lintersection:
            continue
        else:
            dst.write(line)
