#Дано целое число A. Проверить истинность высказывания: «Число A является четным».

def is_even(number):
    return (number % 2) == 0

print(is_even(int(input('введи число : '))))