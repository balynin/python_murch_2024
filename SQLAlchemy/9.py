# Примените несколько функций агрегации и выведите результат на экран

from task6 import Client, Employee, Good, create_engine, sessionmaker, func, session

rec_count = session.query(func.count(Good.good_id)).first()
sum_count = session.query(func.sum(Good.sell_price)).first()
print(rec_count, sum_count)

