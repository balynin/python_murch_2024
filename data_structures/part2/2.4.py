#Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений). Используя операцию деления нацело, найти количество отрезков B, размещенных на отрезке A.

a = int(input("целое положительные число A (A > B)"))
b = int(input("целое положительные число B (A > B)"))

print(a // b, ' количество отрезков B, размещенных на отрезке A')