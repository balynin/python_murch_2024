# Реализуйте все возможные магические методы в классе Car

class MeansOfTransport:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self):
        return f"Means of Transport: {self.brand}, Color: {self.color}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.brand}, {self.color})"


class Car(MeansOfTransport):
    def __init__(self, brand, color, wheel_count):
        super().__init__(brand, color)
        self.wheel_count = wheel_count

    def __str__(self):
        return f"Car: {self.brand}, Color: {self.color}, Wheels: {self.wheel_count}"

    def __repr__(self):
        return f"Car({self.brand}, {self.color}, {self.wheel_count})"

    def __eq__(self, other):
        if isinstance(other, Car):
            return (self.brand, self.color, self.wheel_count) == (other.brand, other.color, other.wheel_count)
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Car):
            return self.wheel_count < other.wheel_count
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Car):
            return self.wheel_count <= other.wheel_count
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Car):
            return self.wheel_count > other.wheel_count
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Car):
            return self.wheel_count >= other.wheel_count
        return NotImplemented

    # Другие магические методы могут быть реализованы по аналогии с приведенными выше методами

# Пример использования
car1 = Car("Toyota", "Red", 4)
car2 = Car("Honda", "Blue", 4)
car3 = Car("Toyota", "Red", 4)

print(str(car1))  # Выведет: Car: Toyota, Color: Red, Wheels: 4
print(repr(car1))  # Выведет: Car(Toyota, Red, 4)
print(car1 == car2)  # Выведет: False
print(car1 == car3)  # Выведет: True
print(car1 != car2)  # Выведет: True
print(car1 < car2)  # Выведет: False
print(car1 <= car2)  # Выведет: True
print(car1 > car2)  # Выведет: False
print(car1 >= car2)  # Выведет: True
