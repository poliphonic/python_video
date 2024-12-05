#!/usr/bin/env python3

import sys
import core
from guess_num import person_guess
from comp_guess_num import comp_guess

core.save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Нужно выбрать команду, наберите help, если вам нужна подсказка')
else:
    if command == 'copy':
        try:
            core.copy_item(sys.argv[2], sys.argv[3])
        except IndexError:
            print('Для выполнения этой функции необходимо указать два '
                  'параметра')
    elif command == 'create_d':
        try:
            core.create_dir(sys.argv[2])
        except IndexError:
            print('Уточните название директории')
    elif command == 'create_f':
        try:
            core.create_file(sys.argv[2])
        except IndexError:
            print('Уточните название файла')
    elif command == 'change':
        try:
            core.change_dir(sys.argv[2])
        except IndexError:
            print('Уточните путь назначения')
    elif command == 'delete':
        try:
            core.delete_item(sys.argv[2])
        except IndexError:
            print('Уточните название объекта')
    elif command == 'list':
        core.get_list()
    elif command == 'play':
        try:
            if sys.argv[2] == 'user':
                person_guess()
            elif sys.argv[2] == 'comp':
                comp_guess()
        except IndexError:
            print('Уточните, кто будет угадывать число')
    elif command == 'help':
        print('list - список файлов и директорий')
        print('create_d - создание директории')
        print('create_f - создание файла')
        print('copy - копирование файла или директории')
        print('delete - удаление файла или директории')
        print('change - изменение текущей директории')
        print('play - игра "Угадай число", уточните, кто угадывает, через '
              'пробел')
        print('user - угадывает пользователь, comp - угадывает компьютер')
    
core.save_info('Конец')
