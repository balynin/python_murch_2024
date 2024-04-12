# Обновите любые данные в таблице клиенты

from task6 import Good, session

query = session.query(Good)
query = query.filter(Good.good_id == 1)
query.update({
    Good.quantity: Good.quantity + 20,
    Good.sell_price: Good.sell_price - 2
})
cc = query.first()
print(cc.quantity, cc.sell_price)