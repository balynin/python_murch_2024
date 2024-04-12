# Создайте новую бд . Напишите коннектор для подключения к базе данных postgresql.

from sqlalchemy import create_engine

engine = create_engine(
    'postgresql+psycopg2://postgres:postgres@localhost/my_sales2',
    #'sqlite:///:memory:',
    echo=True, pool_size=6, max_overflow=10
)
engine.connect()

print(engine)