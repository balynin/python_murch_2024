#Дано целое число A. Проверить истинность высказывания: «Число A является положительным».

def is_positive(number):
    return number > 0

print(is_positive(int(input('введи число : '))))