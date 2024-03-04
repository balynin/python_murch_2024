# Вывести значения функции y=x^2 от 1 до 10 с шагом 0.5.

import numpy as np
def function(x):
    return x ** 2

for i in np.arange(1, 10, 0.5):
    y = function(i)
    print('y = ', y, sep='')

