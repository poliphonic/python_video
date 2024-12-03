#!/usr/bin/env python3

import random


def person_guess():
    number = random.randint(1, 100)
    print('Угадай число от 1 до 100.')
    guess = int(input())
    while guess != number:
        print('>' if number > guess else '<')
        guess = int(input())
    print(f'Победа! Загаданное число {number}')


if __name__ == '__main__':
    person_guess()
