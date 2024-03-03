#Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».

def is_odd(number):
    return (number % 2) == 1

print(is_odd(int(input('введи число : '))))