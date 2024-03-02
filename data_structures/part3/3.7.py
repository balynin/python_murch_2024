def is_true(a, b, c):
    return  a < b < c

a = int(input('введи число a : ' ))
b = int(input('введи число b : ' ))
c = int(input('введи число c : ' ))
print(is_true(a, b, c))