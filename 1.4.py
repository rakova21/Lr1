#   Отсортируйте словарь по значению в порядке возрастания и
#   убывания.

from random import randint
dictionary = {key: randint(1, 20) for key in range(5)} # Генерация случайного словаря
print(dictionary)
# Сортировка по значению в порядке возрастания
sorted_min_max = dict(sorted(dictionary.items(), key=lambda x: x[1]))
print("\nСортировка по значению в порядке возрастания:")
print(sorted_min_max)

# Сортировка по значению в порядке убывания
sorted_max_min = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
print("\nСортировка по значению в порядке убывания:")
print(sorted_max_min)