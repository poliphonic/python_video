#!/usr/bin/env python3

# Давайте опишем пару сущностей player и enemy через словарь, который
# будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# Поэкспериментируйте со значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2). Примечание: имена
# аргументов можете указать свои. Функция в качестве аргумента будет
# принимать атакующего и атакуемого. В теле функция должна получить
# параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения. Новый
# параметр - armor = 1.2 (величина брони персонажа). Надо добавить новую
# функцию, которая будет вычислять и возвращать полученный урон по формуле
# damage / armor

import random


def new_damage(fighter, defender):
    fighter['damage'] = round(fighter['damage'] / defender['armor'])


def attack(fighter, defender):
    defender['health'] -= fighter['damage']


name = ['Джонни Кейдж', 'Скорпион', 'Саб-Зиро', 'Рептилия', 'Кано', 'Райден',
        'Лю Кан', 'Шан Цзун', 'Соня Блейд']
health = [random.randint(100, 200) for _ in range(2)]
damage = [random.randint(2, 100) for _ in range(2)]
armor = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]
random.shuffle(name)
random.shuffle(armor)
player = {'name': name[0], 'health': health[0], 'damage': damage[0],
          'armor': armor[0]}
enemy = {'name': name[1], 'health': health[1], 'damage': damage[1],
         'armor': armor[1]}
print('\nПротивники - {} и {}!'.format(player['name'], enemy['name']))
print(f"{player['name']} - здоровье {player['health']}, урон "
      f"{player['damage']}, броня {player['armor']}")
print(f"{enemy['name']} - здоровье {enemy['health']}, урон {enemy['damage']}, "
      f"броня {enemy['armor']}")
new_damage(player, enemy)
new_damage(enemy, player)
round_num = 1
while player['health'] and enemy['health']:
    print('\n\t\t', round_num, 'раунд!')
    attack(player, enemy)
    print(f"{player['name']} наносит удар силой {player['damage']}")
    enemy['health'] = 0 if enemy['health'] < 0 else enemy['health']
    print(f"{enemy['name']} - оставшееся здоровье {enemy['health']}")
    attack(enemy, player)
    print(f"{enemy['name']} наносит удар силой {enemy['damage']}")
    player['health'] = 0 if player['health'] < 0 else player['health']
    print(f"{player['name']} - оставшееся здоровье {player['health']}")
    round_num += 1
if not player['health'] and not enemy['health']:
    print('\nБой кончился вничью!')
elif not player['health']:
    print(f"\nБой кончился! Победитель - {enemy['name']}!")
elif not enemy['health']:
    print(f"\nБой кончился! Победитель - {player['name']}!")
