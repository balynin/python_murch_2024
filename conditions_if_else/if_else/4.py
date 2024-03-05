# Даны три числа. Найти наименьшее из них.

a = int(input('Введите первое число  '))
b = int(input('Введите второе число  '))
c = int(input('Введите третье число  '))

if a < b:
    min = a
else: min = b
if c < min:
    min = c
print(min)