# Получите данные из таблицы и выведите на экран.

from sqlalchemy import create_engine, select, Table
from task3 import client, supply, provider, good, employee, order, engine

# engine = create_engine(
#     #'postgresql+psycopg2://postgres:postgres@localhost/my_sales2',
#     'sqlite:///:memory:',
#     echo=True, pool_size=6, max_overflow=10
# )
conn = engine.connect()

s = select(good)#.where(good.c.good_id == 1)
print(s)
rs = conn.execute(s)
for row in rs:
    print(row)


print(type(client))