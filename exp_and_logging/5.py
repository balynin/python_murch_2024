#Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0. Если дискриминант отрицателен, программа должна выдать ошибку и предложить пользователю попробовать еще раз с другими коэффициентами. При выполнении скрипта в лог должна записываться информация о успехе или неудаче операции.

from math import sqrt
import logging
logging.basicConfig(level=logging.INFO, filename="py_log5.log", filemode="w")

while True:
    try:
       a = float(input('a = '))
       b = float(input('b = '))
       c = float(input('c = '))

       d = b**2 - 4 * a * c

       if d > 0:
           x1 = (-b + sqrt(d) / (2 * a))
           x2 = (-b - sqrt(d) / (2 * a))
           print(f'x1 = {x1:.2f}; x2 = {x2:.2f}')
           logging.info('all fine')
       elif d == 0:
           x1 = -b / (2 * a)
           print(f'x1 = {x1:.2f}')
           logging.info('all fine')

       elif d < 0:
          raise Exception
    except Exception:
       logging.error('DNegativeError', exc_info=True)
       print('D отрицательный')