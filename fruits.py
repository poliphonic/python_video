#!/usr/bin/env python3

# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих
# исходных списках.

from random import sample
fruits = ['apple', 'apricot', 'banana', 'blueberries', 'cherry', 'coconut',
          'grape', 'kiwi', 'mango', 'orange', 'pear', 'pineapple', 'plum',
          'strawberry', 'tangerine', 'watermelon']
basket1, basket2 = sample(fruits, 9), sample(fruits, 9)
print('In first basket are', ', '.join(basket1) + '.')
print('In second basket are', ', '.join(basket2) + '.')
print('In both baskets are', ', '.join([f for f in basket1 if f in basket2]) + '.')
