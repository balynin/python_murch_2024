# В классе Car добавьте переменную класса car_drive = 4 и реализуйте classmethod, который выводит на экран переменную car_drive

from MeansOfTransport import MeansOfTransport

class Car(MeansOfTransport):
    car_drive = 4  # Переменная класса

    def __init__(self, brand, color, wheel_count):
        super().__init__()

    @classmethod
    def print_car_drive(cls):
        print(f"Car drive: {cls.car_drive}")

# Использование classmethod
Car.print_car_drive()  # Выведет: Car drive: 4

# Создание экземпляра класса Car и вызов classmethod
car = Car("Toyota", "Red", 4)
car.print_car_drive()  # Выведет: Car drive: 4
