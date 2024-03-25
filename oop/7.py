# Попробуйте инициализировать несколько любых переменных в классе Car и сделайте одну переменную приватной, одну защищенной. Попробуйте получить к ним доступ. Какой результат?

from MeansOfTransport import MeansOfTransport

class Car(MeansOfTransport):
    def __init__(self, brand, color, wheel_count, private_var, protected_var):
        super().__init__()
        self._private_var = private_var
        self._protected_var = protected_var

    def get_protected_var(self):
        return self._protected_var

# Инициализация объекта класса Car
car = Car("Toyota", "Red", 4, "Private Value", "Protected Value")

# Прямой доступ к приватной переменной невозможен
try:
    print(car._private_var)
except AttributeError as e:
    print(f"Error: {e}")

# Доступ к защищенной переменной можно получить через метод класса
print(car.get_protected_var())  # Выведет: Protected Value
