class Thing:
    who_am_i = 'I am just a thing'

    def __new__(cls, name, *args, **kwargs):
        if 't' in name:
            raise ValueError('name can not contain letter t')
        else:
            return object.__new__(cls)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.__class__.who_am_i} and my name is {self.name}'

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}>'


class Device(Thing):
    who_am_i = 'I am a modern device'

    def __init__(self, name, price):
        super().__init__(name)
        self.price = price

    def __ge__(self, other):
        return self.price > other.price


class Candy(Thing):
    who_am_i = 'I am a sweet candy'

    def __init__(self, name, taste, price):
        super().__init__(name)
        self.taste = taste
        self.price = price

    def __ge__(self, other):
        return self.price > other.price


class Order:
    who_am_i = 'I am an order with good things'
