#Дано двузначное число. Найти сумму и произведение его цифр.

a = int(input("двузначное число : "))

print('сумма десятков и единиц ', (a // 10) + (a % 10))
print('произведение десятков и единиц ', (a // 10) * (a % 10))