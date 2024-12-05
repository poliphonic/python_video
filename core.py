#!/usr/bin/env python3

import os
import shutil
import datetime


def change_dir(name):
    try:
        os.chdir(name)
    except FileNotFoundError:
        print('Невозможно найти путь')


def copy_item(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая директория уже существует')
    else:
        shutil.copy(name, new_name)


def create_dir(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая директория уже существует')


def create_file(name, text=None):
    with open(name, 'w') as f:
        if text:
            f.write(text)


def delete_item(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def get_list(dirs_only=False):
    lst = os.listdir('.')
    if dirs_only:
        lst = [d for d in lst if os.path.isdir(d)]
    print(lst)
    

def save_info(message):
    with open('log.txt', 'a') as f:
        f.write(f'{datetime.datetime.now()} - {message}' + '\n')


if __name__ == '__main__':
    get_list()
    get_list(True)
    create_dir('test')
    create_file('test.txt', 'some text')
    create_file('test1.txt')
    copy_item('test', 'test1')
    copy_item('test.txt', 'test')
    copy_item('test1.txt', 'test1')
    delete_item('test/test.txt')
    delete_item('test1/test1.txt')
    delete_item('test.txt')
    delete_item('test1.txt')
    delete_item('test')
    delete_item('test1')
    print(os.getcwd())
    change_dir('/home/poli/')
    print(os.getcwd())
    save_info('OK')
