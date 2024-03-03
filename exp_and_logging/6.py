# Написать программу для генерации случайных чисел в заданном диапазоне. Если пользователь ввел недопустимые границы диапазона (например, меньше нуля), программа должна вывести ошибку и попросить ввести диапазон заново. Информация об ошибках должна быть записана в лог.

import random
import logging
logging.basicConfig(level=logging.INFO, filename="py_log6.log", filemode="w")

n1 = int(input('Верхний порог от 0 до 99 : '))
n2 = int(input('Нижний порог от 0 до 99 : '))
rand_list = []
n = 30
for i in range(n):
	rand_list.append(random.randint(n1, n2))
print(rand_list)
