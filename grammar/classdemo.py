class Iron:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("iron " + self.name)


class Wheel:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("wheel " + self.name)


class Car(Wheel, Iron):
    def __init__(self, name):
        super().__init__(name)
        super(Car, self).__init__(name)
        super(Wheel, self).__init__(name)

        # Wheel.__init__(self, name)
        # Iron.__init__(self, name)

        self.name = name
        # self.print_name()

    def print_name(self):
        print(self.name)
        super(Car, self).print_name()
        super(Wheel, self).print_name()

        # Iron.print_name(self)

        # print("aaaaa")
        # car = Car("mmm")
        # car.print_name()
