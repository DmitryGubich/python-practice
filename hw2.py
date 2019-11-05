# Задания по структурам данных
import collections

# Написать фрагмент кода, который принимает список чисел и возвращает сумму этих чисел.
try:
    input_list = [int(i) for i in input('Введите последовательность чисел:').split()]
except ValueError:
    print('Проверьте ввод')
else:
    print('Сумма элементов списка:', sum(input_list))
print('*' * 150)

# Написать фрагмент кода, который принимает список чисел и возвращает максимальный и минимальный элементы.
try:
    input_list = [int(i) for i in input('Введите последовательность чисел:').split()]
except ValueError:
    print('Проверьте ввод')
else:
    print('Максимальное число:', max(input_list))
    print('Минимальное число:', min(input_list))
print('*' * 150)

# Написать фрагмент кода, который принимает список элементов и возвращает список уникальных элементов.
try:
    input_list = [int(i) for i in input('Введите последовательность чисел:').split()]
except ValueError:
    print('Проверьте ввод')
else:
    print('Уникальные элементы:', set(input_list))
print('*' * 150)

# Написать фрагмент кода, который принимает строку и возвращает перевернутую версию этой строки ('hello' → 'olleh').
input_string = input('Введите строку:')
# 1
result = ""
for i in input_string:
    result = i + result
print('Функция: ', result)
# 2
print('Slice: ', input_string[::-1])
# 3
print('Reversed: ', "".join(reversed(input_string)))
print('*' * 150)

# Написать фрагмент кода, который принимает два списка и возвращает список, который
# состоит из элементов как первого списка, так и второго (['hello', 'hi'], ['hi', 'bye'] → ['hello', 'hi', 'bye']).
try:
    input_list_1 = [int(i) for i in input('Введите последовательность чисел:').split()]
    input_list_2 = [int(i) for i in input('Введите последовательность чисел:').split()]
except ValueError:
    print('Проверьте ввод')
else:
    # 1
    print('Общий список 1:', input_list_1 + input_list_2)
    # 2
    print('Общий список 2:', [*input_list_1, *input_list_2])
print('*' * 150)

# Написать фрагмент кода, который принимает в качестве аргумента строку и возвращает список слов,
# из которых состоит строка ('hi hi bye bye bye' → ['hi', 'bye']).
input_string = set(input('Введите строку:').split())
print('Элементы: ', list(set(input_string)))
print('*' * 150)

# Написать фрагмент кода, который принимает в качестве агрумента строку и возвращает словарь.
# Ключом словаря являются слово, которые встречается в строке, а значением - сколько раз это слово встречается
# в строке ('hi hi bye bye bye' → {'hi': 2, 'bye': 3}).
result = {}
input_list = input('Введите строку: ').split()
# 1
for element in input_list:
    try:
        result[element] += 1
    except KeyError:
        result[element] = 1
print('Наш словарь: ', result)
# 2
result = {}
for element in input_list:
    result[element] = result.get(element, 0) + 1
print('Наш словарь: ', result)
# 3
c = collections.Counter(input_list)
print('Counter: ', dict(c))
print('*' * 150)

# Написать фрагмент кода, который принимает список элементов и возвращает список только тех элементов,
# которые встречаются несколько раз в списке.
dictionary = {}
result = []

input_list = [int(i) for i in input('Введите последовательность чисел:').split()]
# 1
for element in input_list:
    try:
        dictionary[element] += 1
    except KeyError:
        dictionary[element] = 1
for k, v in dictionary.items():
    if v > 1:
        result.append(k)
print(result)
print('*' * 150)
