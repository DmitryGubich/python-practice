class MyObject:

    def __new__(cls, name, *args, **kwargs):
        print(f"__new__ magic method from {cls.__name__} is called")
        if 'z' in name:
            raise ValueError('name can not contain letter z')
        else:
            return object.__new__(cls)

    def __init__(self, name):
        print(f"__init__ magic method from {self.__class__.__name__} is called")
        self.name = name


if __name__ == '__main__':
    MyObject('name z')
