#!/usr/bin/env python3

# Создайте модуль. В нем создайте функцию, которая принимает список и
# возвращает из него случайный элемент. Если список пустой функция должна
# вернуть None. Проверьте работу функций в этом же модуле.

from random import choice


def random_element(seq):
    return choice(seq) if seq else None


if __name__ == '__main__':
    print(random_element([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(random_element([]))
