class MyObject:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


if __name__ == "__main__":
    shop = MyObject()
    shop1 = MyObject()
    print(shop)
    print(shop1)
    print(shop == shop1)
    print(shop is shop1)
