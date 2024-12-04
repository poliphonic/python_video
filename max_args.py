#!/usr/bin/env python3

# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее
# из них.

def max_args(*args):
    return max(args)


print(max_args(-18, 116, 0))
