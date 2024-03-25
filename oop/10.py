# Реализуйте класс Calculator, в котором будет один метод, для вычисления суммы двух чисел.
# Реализуйте еще один класс, который будет наследоваться от класса Calculator и перегрузите метод для вычисления суммы двух чисел, чтобы он делал конкатенацию двух строк.


class Calculator:
    def sum(self, a, b):
        return a + b

class StringCalculator(Calculator):
    def sum(self, a, b):
        return str(a) + str(b)

# Пример использования
calc = Calculator()
print(calc.sum(5, 3))  # Выведет: 8

str_calc = StringCalculator()
print(str_calc.sum("Hello, ", "ITMentor"))  # Выведет: Hello, World!
