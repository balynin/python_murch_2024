# Посчитайте сумму столбца Rachel1 из файла bikes.csv

import pandas as pd

fr = pd.read_csv('bikes.csv')
print(fr['Rachel1'])
print(sum(fr['Rachel1']))

