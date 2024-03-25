# Работаем с классом из 3 пункта. Реализуйте сеттеры и геттеры для цвета и марки транспортного средства.

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

car = MeansOfTransport("Toyota", "Red")
print(car.brand)
print(car.color)

car.brand = "Honda"
car.color = "Blue"

print(car.brand)
print(car.color)  
