class Distance:
    def __init__(self):
        self.__distance = 0.0

    @property
    def in_metres(self):
        return self.__distance

    @in_metres.setter
    def in_metres(self, val):
        self.__distance = float(val)

    @property
    def in_feet(self):
        return self.__distance * 3.2808399

    @in_feet.setter
    def in_feet(self, val):
        self.__distance = float(val) / 3.2808399


if __name__ == "__main__":
    distance = Distance()
    distance.in_metres = 1000.0
    print(distance.in_metres)
    print(distance.in_feet)
    distance.in_feet = 1000
    print(distance.in_metres)
    print(distance.in_feet)
