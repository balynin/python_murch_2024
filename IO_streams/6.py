import pandas as pd

# подключаем модуль pathlib и библиотеку Path модуля pathlib
import pathlib
from pathlib import Path

# Получаем строку, содержащую путь к рабочей директории:
work_path = pathlib.Path.cwd()

# сохраним путь к csv файлу в переменной data_path
data_path = Path(work_path, 'bikes.csv')

# Загружаем данные из csv файла в переменную data
data = pd.read_csv(data_path)

print(data.head(10))
