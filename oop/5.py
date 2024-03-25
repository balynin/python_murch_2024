# Реализуйте два класса Car и Moped, которые будут наследоваться от класса MeansOfTransport. При инициализации они должны принимать новый аргументы(количество колес.

class MeansOfTransport:
    def __init__(self, brand, color):
        self._brand = brand
        self._color = color

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def show_color(self):
        print(f"цвет машины: {self._color}")

    def show_brand(self):
        print(f"марка машины: {self._brand}")

class Car(MeansOfTransport):
    def __init__(self, brand, color, wheel_count):
        super().__init__(brand, color)
        self._wheel_count = wheel_count

    @property
    def wheel_count(self):
        return self._wheel_count

    @wheel_count.setter
    def wheel_count(self, value):
        self._wheel_count = value


class Moped(MeansOfTransport):
    def __init__(self, brand, color, wheel_count):
        super().__init__(brand, color)
        self._wheel_count = wheel_count

    @property
    def wheel_count(self):
        return self._wheel_count

    @wheel_count.setter
    def wheel_count(self, value):
        self._wheel_count = value


# Пример использования классов Car и Moped
car = Car("Toyota", "Red", 4)
print(car.brand)  # Выведет: Toyota
print(car.color)  # Выведет: Red
print(car.wheel_count)  # Выведет: 4

moped = Moped("Harley Davidson", "Black", 2)
print(moped.brand)  # Выведет: Harley Davidson
print(moped.color)  # Выведет: Black
print(moped.wheel_count)  # Выведет: 2
