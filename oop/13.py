# Реализуйте класс Dog. Придумайте, какие переменные будет принимать данный класс и какие методы будут реализованы. Реализуйте в этом классе паттерн Singleton


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Dog(metaclass=Singleton):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} {self.breed} сказал Гав-гав!"


# Пример использования
dog1 = Dog("Rex", "German Shepherd")
dog2 = Dog("Max", "Bulldog")

print(dog1.bark())
print(dog2.bark())