#Дано двузначное число. Вывести вначале его левую цифру (десятки), а затем — его правую цифру (единицы). Для нахождения десятков использовать операцию деления нацело, для нахождения единиц — операцию взятия остатка от деления.

a = int(input("двузначное число : "))

print('десятки ', a // 10, 'единицы ', a % 10)