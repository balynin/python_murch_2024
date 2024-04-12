#Сделайте несколько Inner join запросов и выведите на экран результат.


from task6 import Client, Good, session

query = session.query(Good, Client).join(Client, Good.good_id == Client.client_id).all()
for row in query:
    print(row)
