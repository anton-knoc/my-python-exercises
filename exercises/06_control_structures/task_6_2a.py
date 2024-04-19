# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_addr = input("Enter IP address:")
ip_actets = ip_addr.split('.')
ip_actets_int = []

for i in ip_actets:
    try:
        int(i)
    except ValueError:
        break
    if int(i) <= 255 :
        ip_actets_int.append(int(i))

if len(ip_actets_int) == 4 :
    ip = ip_actets_int[0]
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

else:
    print('Неправильный IP-адрес')