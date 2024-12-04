#!/usr/bin/env python3

# Создайте модуль. В нем создайте функцию, создающую директории от dir_1
# до dir_9 в папке, из которой запущен данный код. Затем создайте вторую
# функцию, удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os


def make_dirs():
    for i in range(1, 10):
        os.mkdir('dir_{}'.format(i))

      
def del_dirs():
    for i in range(1, 10):
        os.rmdir('dir_{}'.format(i))
        
        
if __name__ == '__main__':
    make_dirs()
    del_dirs()
