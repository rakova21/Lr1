#   Дан список [1,34, ’qwerty’, 12, 13, 16, ’Love’, ’Python’]. Создать
#   отдельно список из слов и отдельно из чисел. В числовом списке найти
#   сумму и произведение всех элементов. Вывести на экран три
#   наибольших элемента.


spis = [1,34,'qwerty', 12, 13, 16, 'Love','Python']    # Исходный список
print("Исходный список:",spis)

# Создание списка из слов
words = [item for item in spis if isinstance(item, str)]
print("Список из слов:",words)

# Создание списка из чисел
numbers = [item for item in spis if isinstance(item, int)]
print("Список из чисел:",numbers)

# Нахождение суммы чисел
sum_of_numbers = sum(numbers)
print("Сумма чисел:", sum_of_numbers)

# Нахождение произведения чисел
product_of_numbers = 1
for i in numbers:
    product_of_numbers *= i
print("Произведение чисел:", product_of_numbers)

# Вывод трех наибольших элементов
sorted_list = sorted(numbers, reverse=True)     # Cортировка числового списка в порядке убывания
print("Три наибольших элемента:", sorted_list[:3])  # Вывод первых трех чисел из отсортированного списка