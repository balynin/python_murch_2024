#Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A > 2 и B ≤ 3».

def is_true(num1, num2):
    return num1 > 2 and num2 <= 3

num1 = int(input('введи число1 : ' ))
num2 = int(input('введи число2 : ' ))
print(is_true(num1, num2))