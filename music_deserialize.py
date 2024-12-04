#!/usr/bin/env python3

# Создать модуль music_deserialize.py. В этом модуле открыть файлы .json и
# .pickle, прочитать из них информацию. И получить объект: словарь из
# предыдущего задания.

import pickle
import json
with open('son_lux.pickle', 'rb') as fp:
    print(pickle.load(fp))
with open('son_lux.json', 'r') as fj:
    print(json.load(fj))
