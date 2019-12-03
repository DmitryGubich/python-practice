from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Triangle(Figure):
    def __init__(self, x, y, z):
        super().__init__()
        self.sides = (x, y, z)

    def draw(self):
        return "This is a triangle which sides are {}".format(self.sides)


class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def draw(self):
        return "This is a square with side {}".format(self.side)


if __name__ == "__main__":
    a = Triangle(3, 4, 5)
    b = Square(4)
    list_of_figures = [a, b]
    for figure in list_of_figures:
        print(figure.draw())
