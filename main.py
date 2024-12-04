#!/usr/bin/env python3

# Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2
# сделайте импорт в main.py всех функций. Вызовите каждую функцию в
# main.py и проверьте что все работает как надо.

import dir_master
from random_element import random_element

if __name__ == '__main__':
    dir_master.make_dirs()
    dir_master.del_dirs()
    print(random_element([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(random_element([]))
