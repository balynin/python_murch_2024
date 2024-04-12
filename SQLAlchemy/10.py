# Удалите несколько строк из таблицы Поставщик и выведите на экран строки этой таблицы


from task6 import Provider, session

query = session.query(Provider)
query = query.filter(Provider.provider_id > 4)
query.delete()
session.commit()
