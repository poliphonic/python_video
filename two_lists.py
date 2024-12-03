#!/usr/bin/env python3

# Даны два произвольных списка. Удалите из первого списка элементы
# присутствующие во втором списке.

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
for item in my_list_2:
    while item in my_list_1:
        my_list_1.remove(item)
