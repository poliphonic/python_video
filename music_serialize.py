#!/usr/bin/env python3

# Создать модуль music_serialize.py. В этом модуле определить словарь для
# вашей любимой музыкальной группы. С помощью модулей json и pickle
# сериализовать данный словарь в json и в байты, вывести результаты в
# терминал. Записать результаты в файлы .json и .pickle. В файле .json
# указать кодировку utf-8.

import pickle
import json
son_lux = {'name': 'Son Lux',
           'members': ['Ryan Lott', 'Rafiq Bhatia', 'Ian Chang'],
           'albums': [{'name': 'At War with Walls & Mazes', 'year': 2008},
                      {'name': 'We Are Rising', 'year': 2011},
                      {'name': 'Lanterns', 'year': 2013},
                      {'name': 'Original Music from and Inspired By: The '
                               'Disappearance of Eleanor Rigby', 'year': 2014},
                      {'name': 'Bones', 'year': 2015},
                      {'name': 'Brighter Wounds', 'year': 2018},
                      {'name': 'Tomorrows I', 'year': 2020},
                      {'name': 'Tomorrows II', 'year': 2020},
                      {'name': 'Tomorrows III', 'year': 2021}]}
print(pickle.dumps(son_lux))
print(json.dumps(son_lux))
with open('son_lux.pickle', 'wb') as fp:
    pickle.dump(son_lux, fp)
with open('son_lux.json', 'w', encoding='utf-8') as fj:
    json.dump(son_lux, fj)
