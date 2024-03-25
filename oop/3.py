# Создайте класс {{MeansOfTransport }}(для определения цвета и марки машины), принимающий 2 аргумента при инициализации (марка и цвет транспортного стредства). В этом классе реализуйте методы show_color(), выводящий на печать цвет транспортного средства и show_brand, для получения марки транспортного средства.

class MeansOfTransport:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_color(self):
        print(f"цвет машины: {self.color}")

    def show_brand(self):
        print(f"марка машины: {self.brand}")


car = MeansOfTransport("Toyota", "Red")
car.show_color()
car.show_brand()  # Выведет:
