#Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B находится между числами A и _C_».

def is_true(a, b, c):
    return  a < b < c

a = int(input('введи число a : ' ))
b = int(input('введи число b : ' ))
c = int(input('введи число c : ' ))
print(is_true(a, b, c))