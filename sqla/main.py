from db_init import *


# 2 Создайте новую бд . Напишите коннектор для подключения к базе данных postgresql.
print(engine)

# 3 Создайте Классы моделей, которые будут реализовывать схему данных на прикрепленном рисунке.
#  СМОТРЕТЬ db_init.py

# 4 Заполните ĸаждую таблицу минимум 5 строĸами данных.
#  СМОТРЕТЬ db_create_and_fill.py

# 5 Получите данные из таблицы и выведите на экран.
query = session.query(Good).where(Good.good_id == 1)
for row in query:
    print(row)

# 6 Сделайте несколько Inner join запросов и выведите на экран результат.
query = session.query(Good, Client).join(Client, Good.good_id == Client.client_id).all()
for row in query:
    print(row)

# 7 Обновите любые данные в таблице клиенты.
query = session.query(Good)
query = query.filter(Good.good_id == 1)
query.update({
    Good.quantity: Good.quantity + 20,
    Good.sell_price: Good.sell_price - 2
})
res = query.first()
print(res.quantity, res.sell_price)

# 8 # Получите данные вместе с WHERE, ORDER BY, GROUP BY, DISTINCT и выведите на экран.
res = session.query(Good).filter_by(good_name="1971-04-04").first()
print(res)


# 9 Примените несколько функций агрегации и выведите результат на экран
rec_count = session.query(func.count(Good.good_id)).first()
sum_count = session.query(func.sum(Good.sell_price)).first()
print(rec_count, sum_count)

# 10 Удалите несколько строк из таблицы Поставщик и выведите на экран строки этой таблицы
query = session.query(Provider)
query = query.filter(Provider.provider_id > 4)
query.delete()
session.commit()

query = session.query(Provider)
for row in query:
    print(row)
