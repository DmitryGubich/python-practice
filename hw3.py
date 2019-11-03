import math
from functools import wraps


# Напишите функцию, которая осуществляет проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.


def is_palindrome(text):
    """ Является ли слово палиндромом """
    return text == text[::-1]


# Написать функцию, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.
def square_params(a):
    """ Возвращаю информацию о квадрате """
    return 4 * a, a ** 2, a * math.sqrt(2)


# Пользователь делает вклад в размере amount рублей сроком на years лет под 10% годовых
# (каждый год размер его вклада увеличивается на percent %. Эти деньги прибавляются к сумме вклада,
# и на них в следующем году тоже будут проценты). Написать функцию bank, принимающая аргументы amount, years и percent
# и возвращающую сумму, которая будет на счету пользователя.
def bank(amount, years, percent):
    """ Рассчитываю депозит """
    result = amount
    for _ in range(years):
        result += amount * (percent / 100)
    return result


# Написать декоратор, который будет приводить передаваемый во внутреннюю функцию текст к верхнему регистру
def my_decorator(func):
    """ Я возвращаю текст в верхнем регистре """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """ Я внутренняя функция для декоратора """
        return func(*args, **kwargs).upper()

    return wrapper


# Пример с обсластью видимости
test_variable = 'initial global value'


def test_function_scopes():
    """Scopes and Namespaces Example"""

    test_variable = 'initial value inside test function'

    def do_local():
        # Create variable that is only accessible inside current do_local() function.
        test_variable = 'local value'
        return test_variable

    def do_nonlocal():
        # Address the variable from outer scope and try to change it.
        nonlocal test_variable
        test_variable = 'nonlocal value'
        return test_variable

    def do_global():
        # Address the variable from very global scope and try to change it.
        global test_variable
        test_variable = 'global value'
        return test_variable

    # On this level currently we have access to local for test_function_scopes() function variable.
    assert test_variable == 'initial value inside test function'

    # Do local assignment.
    # It doesn't change global variable and variable from test_function_scopes() scope.
    do_local()
    assert test_variable == 'initial value inside test function'

    # Do non local assignment.
    # It doesn't change global variable but it does change variable
    # from test_function_scopes() function scope.
    do_nonlocal()
    assert test_variable == 'nonlocal value'

    # Do global assignment.
    # This one changes global variable but doesn't change variable from
    # test_function_scopes() function scope.
    do_global()
    assert test_variable == 'nonlocal value'


def test_global_variable_access():
    """Testing global variable access from within a function"""

    # Global value of test_variable has been already changed by do_global() function in previous
    # test so let's check that.
    global test_variable
    assert test_variable == 'global value'


# Написать декоратор, который выводит текст внутренней функции несколько раз.
def repeat(times):
    """ Повторить вызов times раз, и вернуть среднее значение """

    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            for i in range(times):
                print(func(*args, **kwargs))

        return decorated

    return decorator


# Написать кэширующий декоратор, который сохраняет значение функции при каждом вызове.
# При повторном вызове функции возвращается сохраненное значение.
def cache_decorator(func):
    """ Кэширующий декоратор """
    cache = {}

    @wraps(func)
    def inner(*args):
        if args in cache:
            print('Берём значение из кэша')
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return inner


# TODO: последнее задание: переписать всё с использование пакетов !!!

# Добавить main только в самом конце, после объяснения модулей
if __name__ == '__main__':
    print(is_palindrome.__doc__)
    print(is_palindrome('шалаш'))
    print('*' * 150)

    print(square_params.__doc__)
    print(square_params(5))
    print('*' * 150)

    print(bank.__doc__)
    print(bank(amount=1000, years=20, percent=10))
    print('*' * 150)


    @my_decorator
    def hello_world():
        """ Я возвращаю сообщение 'Hello world!' """
        return 'Hello world!'

    print(hello_world.__doc__)
    print(hello_world())
    print('*' * 150)


    @repeat(5)
    def print_something(text):
        """ Я возвращаю сообщение """
        return text

    print(print_something.__doc__)
    print_something('Всем привет')
    print('*' * 150)


    @cache_decorator
    def sum_two(first, second):
        """ Я возвращаю сумму двух элементов """
        return first + second

    print(sum_two.__doc__)
    print(sum_two(1, 2))
    print(sum_two(2, 3))
    print(sum_two(22, 16))
    print(sum_two(2, 3))
    print(sum_two(1, 2))
    print('*' * 150)
