# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
    ip_addr = input("Enter IP address:")
    ip_actets = ip_addr.split('.')
    ip_correct = True

    if len(ip_actets) == 4 :
        for i in ip_actets:
            if not (i.isdigit() and int(i) <= 255):
                ip_correct = False
                break
    else:
        ip_correct = False
    if ip_correct:
        break
    print('Неправильный IP-адрес')

if ip_addr == '0.0.0.0':
    print('unassigned')
elif ip_addr == '255.255.255.255':
    print('local broadcast')
elif 1 <= int(ip_actets[0]) <= 223:
    print('unicast')
elif 224 <= int(ip_actets[0]) <= 239:
    print('multicast')
else:
    print('unused')






"""
ip_correct = False

while pass_correct == False:
    ip_addr = input("Enter IP address:")
    ip_actets = ip_addr.split('.')
    if len(ip_actets) == 4 :
        for i in ip_actets:
            if i.isdigit() and int(i) <= 255:
                ip_correct = True
            else:
                ip_correct = False
                print('Неправильный IP-адрес')
                break
    else:
        print('Неправильный IP-адрес')

if ip_addr == '0.0.0.0':
    print('unassigned')
elif ip_addr == '255.255.255.255':
    print('local broadcast')
elif 1 <= int(ip_actets[0]) <= 223:
    print('unicast')
elif 224 <= int(ip_actets[0]) <= 239:
    print('multicast')
else:
    print('unused')
"""