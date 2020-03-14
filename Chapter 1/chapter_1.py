class IllegalCarError(Exception):
    """Raise for pax_count and car_mass errors"""

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


class Car:
    def __init__(self, pax_count, car_mass, gear_count):
        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count

    def total_mass(self):
        return self.pax_count*70+self.car_mass

    @property
    def car_mass(self):
        return self._car_mass

    @property
    def pax_count(self):
        return self._pax_count

    @car_mass.setter
    def car_mass(self, value):
        try:
            if value > 2000:
                raise IllegalCarError(
                    "car_mass (excluding the passengers) cannot be greater than 2000 kg.")
        except IllegalCarError as error:
            print("Received error:", error.data)
        self._car_mass = value

    @pax_count.setter
    def pax_count(self, value):
        try:
            if value > 5 or value < 1:
                raise IllegalCarError(
                    "pax_count cannot be greater than 5, or less than 1")
        except IllegalCarError as error:
            print("Received error:", error.data)
        self._pax_count = value


pax_count = int(
    input("Number of passengers riding in the car (including the driver): "))
car_mass = int(
    input("Mass of the empty car (in kg): "))
gear_count = int(
    input("Number of gears:  "))

c = Car(pax_count, car_mass, gear_count)
print(c.total_mass())
