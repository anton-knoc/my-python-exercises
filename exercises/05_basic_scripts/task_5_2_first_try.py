# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

#1st try
#INPUT
network = input('Enter netwrok (X.X.X.X/XX):')
network_list = network.split('/')

#IP
act1, act2, act3, act4 = network_list[0].split('.')
act1 = int(act1)
act2 = int(act2)
act3 = int(act3)
act4 = int(act4)

#MASK
mask = int(network_list[1])
mask_str = "1" * mask + "0" * ( 32 - mask)
mask_act1 = mask_str[0:8]
mask_act2 = mask_str[8:16]
mask_act3 = mask_str[16:24]
mask_act4 = mask_str[24:32]

#OUTPUT
network_template= """
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:>08b}  {1:>08b}  {2:>08b}  {3:>08b}

Mask:
/{4}
{9:<8} {10:<8} {11:<8} {12:<8}
{5:<8}  {6:<8}  {7:<8}  {8:<8}

"""
print(network_template.format(act1, act2, act3, act4, mask, mask_act1, mask_act2, mask_act3, mask_act4,
      int(mask_act1, 2), int(mask_act2, 2), int(mask_act3, 2), int(mask_act4, 2)))
