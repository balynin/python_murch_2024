def is_true(a, b):
    return  ((a % 2) == 1 and (b % 2) != 1) or ((a % 2) != 1 or (b % 2) == 1)

a = int(input('введи число a : ' ))
b = int(input('введи число b : ' ))
print(is_true(a, b))