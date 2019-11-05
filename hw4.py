# Задания по итераторам, генераторам и модулю itertools
# Итератор – любой объект, реализующий метод __next__, который возвращает следующий элемент в очереди или
# выбрасывает исключение StopIteration, если не осталось элементов.
# Итерируемый объект – любой объект, реализующий метод __iter__ или __getitem__.
# Итерируемым объектом является любая коллекция: список, кортеж, словарь, и т.д.
# Цель итерируемого объекта – создать итератор. Для этого у него есть метод __iter__,
# при каждом обращении к которому создается новый итератор.
# Цель итератора – пройтись по элементам. Для этого у него есть метод __next__, 
# который возвращает элементы один за другим.
# Демо с итераторами
def iterator_demo():
    num_list = [1, 2, 3, 4, 5]
    for i in num_list:
        print(i)

    itr = iter(num_list)

    print(type(num_list))
    print(type(itr))

    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    # print(next(itr))


# Напишите свой собственный класс итератор
class CustomIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


def custom_iterator_demo():
    custom_iterator = CustomIterator(3)
    print(next(custom_iterator))
    print(next(custom_iterator))
    print(next(custom_iterator))
    # print(next(custom_iterator))

    print(type(custom_iterator))

    custom_iterator = CustomIterator(5)
    for i in custom_iterator:
        print(i)


def custom_generator(limit):
    counter = 0
    while counter < limit:
        counter += 1
        yield counter
    else:
        raise StopIteration


if __name__ == '__main__':
    iterator_demo()
    print('*' * 150)
    custom_iterator_demo()
    print('*' * 150)
    for i in CustomIterator(10*100_000_000):
        print(i)
    #for i in custom_generator(10*100_000_000):
    #    print(i)
