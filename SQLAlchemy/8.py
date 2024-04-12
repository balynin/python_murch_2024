# Получите данные вместе с WHERE, ORDER BY, GROUP BY, DISTINCT и выведите на экран.

from task6 import Client, Employee, Good, create_engine, sessionmaker, session

record = session.query(Good).filter_by(good_name="1971-04-04").first()
print(record)
