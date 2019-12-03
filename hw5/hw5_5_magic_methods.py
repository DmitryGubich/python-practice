class Thing:
    who_am_i = 'I am just a thing'

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

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price


class Candy(Thing):
    who_am_i = 'I am a sweet candy'

    def __init__(self, name, taste, price):
        super().__init__(name)
        self.taste = taste
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price


class Order:
    who_am_i = 'I am an order with good things'

    def __init__(self, things=None):
        self.things = things or []

    def __str__(self):
        result = []
        for thing in self.things:
            result.append(str(thing))
        return ', '.join(result)

    def __add__(self, other):
        first_things = self.things
        second_things = other.things
        return Order(things=[*first_things, *second_things])

    def __len__(self):
        return len(self.things)

    def __iter__(self):
        return iter(self.things)

    @property
    def total_price(self):
        prices = []
        for thing in self.things:
            prices.append(thing.price)
        return sum(prices)


if __name__ == '__main__':
    candies_list = [
        Candy('sweet', 'mint', 100),
        Candy('tasty', 'strawberries', 150),
    ]
    devices_list = [
        Device('laptop', 550),
        Device('phone', 550),
    ]
    candy_order = Order(things=candies_list)
    device_order = Order(things=devices_list)
    print(candy_order)
    print(device_order)

    cheap_candy = Candy('sweet', 'mint', 100)
    expensive_candy = Candy('tasty', 'strawberries', 150)
    if cheap_candy < expensive_candy:
        print('good')
    if expensive_candy > cheap_candy:
        print('good')

    order = candy_order + device_order
    print(order)
    print(len(order))
    print(order.total_price)

    for item in order:
        print(item)
