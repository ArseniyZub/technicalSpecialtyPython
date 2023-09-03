# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

import random


items = {'bottle_of_water': 2, 'Rucksack': 1, 'Sleeping bag liner': 5, 'thermos': 2, 'clothes': 3}

max_weight = int(input('Введите максимальный вес: '))
possible_items = [] 
count = len(items)

while count:
    thing, weight = random.choice(list(items.items()))

    if weight <= max_weight:
        if thing not in possible_items:
            possible_items.append(thing)
    max_weight -= weight

    count -= 1

print(possible_items)