from sqlalchemy import create_engine, insert
from task3 import client, supply, provider, good, employee, order, engine

# engine = create_engine(
#     #'postgresql+psycopg2://postgres:postgres@localhost/my_sales2',
#     'sqlite:///:memory:',
#     #echo=True, pool_size=6, max_overflow=10
# )
conn = engine.connect()

rows = [
    (1, 'Ivanov Ivan Ivanovich', 'Moskwa Sovetskaya st 67-7', '123-87-43'),
    (2, 'Petrov Petr Petrovich', 'Kostroma Oktyabrya st 65-65', '234-76-43'),
    (3, 'Kozlov Ivan Sergeevich', 'Yaroslavl Sovetskaya st 78-87', '654-09-21'),
    (4, 'Ivanov Petr Ivanovich', 'Ivanovo Oktyabrya st 54-76', '567-87-43'),
    (5, 'Gerasimov Vasilii Ivanovich', 'Moskwa Oktyabrya st 9-5', '098-65-87'),
    (6, 'Soloviev Petr Aleksandrovich', "Kostroma Sovetskaya st 9-6", '345-87-87')
]

stmt = insert(client).values(
    [{'client_id': client_id, 'fio': fio, 'address': address, 'phone': phone} for client_id, fio, address, phone in
     rows])

with engine.begin() as conn:
    conn.execute(stmt)




rows = [
    (1, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (2, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (3, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (4, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (5, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (6, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
]

stmt = insert(provider).values(
    [{'provider_id': provider_id, 'provider_name': provider_name, 'supplier_represent': supplier_represent,
      'ask_to': ask_to, 'phone': phone, 'address': address} for provider_id, provider_name, supplier_represent, ask_to, phone, address in
     rows])

with engine.begin() as conn:
    conn.execute(stmt)

rows = [
    (1, 2, '1971-04-04'),
    (2, 3, '1971-04-04'),
    (3, 1, '1971-04-04'),
    (4, 4, '1971-04-04'),
    (5, 5, '1971-04-04'),
    (6, 6, '1971-04-04')
]

stmt = insert(supply).values(
    [{'supply_id': supply_id, 'provider_id': provider_id, 'date_supply': date_supply} for supply_id, provider_id, date_supply in
     rows])

with engine.begin() as conn:
    conn.execute(stmt)


rows = [
    (1, 2, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', 1, 9, 1, 14),
    (2, 3, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', 1, 9, 1, 14),
    (3, 1, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', 1, 9, 1, 14),
    (4, 4, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', 1, 9, 1, 14),
    (5, 5, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', 1, 9, 1, 14),
    (6, 6, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', 1, 9, 1, 14)
]

stmt = insert(good).values(
    [{'good_id': good_id, 'supply_id': supply_id, 'good_name': good_name, 'specifications': specifications,
      'description': description, 'pic': pic, 'cost_price': cost_price,
      'sell_price': sell_price, 'availably': availably, 'quantity': quantity} for good_id, supply_id, good_name, specifications, description, pic, cost_price, sell_price, availably, quantity in
     rows])

with engine.begin() as conn:
    conn.execute(stmt)



rows = [
    (1, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (2, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (3, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (4, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (5, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (6, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
]

stmt = insert(employee).values(
    [{'employee_id': employee_id, 'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name,
      'positions': positions, 'phone': phone, 'address': address,
      'birthday': birthday} for employee_id, last_name, first_name, middle_name, positions, phone, address, birthday in
     rows])

with engine.begin() as conn:
    conn.execute(stmt)



rows = [
    (1, 2, 3, 4, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (2, 3, 4, 5, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (3, 4, 5, 6, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (4, 5, 6, 1, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (5, 6, 1, 2, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04'),
    (6, 1, 2, 3, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
]

stmt = insert(order).values(
    [{'order_id': order_id, 'employee_id': employee_id, 'good_id': good_id, 'client_id': client_id,
      'positions': positions, 'phone': phone, 'address': address,
      'birthday': birthday} for order_id, employee_id, good_id, client_id, positions, phone, address, birthday in
     rows])

with engine.begin() as conn:
    conn.execute(stmt)