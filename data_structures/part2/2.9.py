#Дано трехзначное число. Используя одну операцию деления нацело, вывести первую цифру данного числа (сотни).

a = int(input("трехзначное число : "))

print((a // 100), 'сотен в этом числе')