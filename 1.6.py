from random import randint

tuple = tuple(randint(1, 10) for _ in range(5))
print(tuple)
print("Первый элемент:", tuple[0])    # Вывод первого элемента
print("Последний элемент:", tuple[-1])    # Вывод последнего элемента