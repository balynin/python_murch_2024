def is_true(num1, num2):
    return num1 >= 0 or num2 < -2

num1 = int(input('введи число1 : ' ))
num2 = int(input('введи число2 : ' ))
print(is_true(num1, num2))