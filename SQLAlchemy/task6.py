from sqlalchemy.orm import declarative_base, sessionmaker, relationship, backref
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, or_, create_engine, func

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/my_sales2')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Client(Base):
    __tablename__ = 'client'

    client_id = Column(Integer(), primary_key=True)
    fio = Column(String(255))
    address = Column(String(255))
    phone = Column(String(255))

    def __init__(self, client_id, fio, address, phone):
        self.client_id = client_id
        self.fio = fio
        self.address = address
        self.phone = phone


class Good(Base):
    __tablename__ = 'good'

    good_id = Column(Integer(), primary_key=True)
    supply_id = Column(Integer(), ForeignKey('supply.supply_id', ondelete="CASCADE"))
    good_name = Column(String(255))
    specifications = Column(String(255))
    description = Column(String(255))
    pic = Column(String(255))
    cost_price = Column(Integer())
    sell_price = Column(Integer())
    availably = Column(Boolean())
    quantity = Column(Integer())


    def __init__(self, good_id, supply_id, good_name, specifications, description, pic, cost_price, sell_price, availably, quantity):
        self.good_id = good_id
        self.supply_id = supply_id
        self.good_name = good_name
        self.specifications = specifications
        self.description = description
        self.pic = pic
        self.cost_price = cost_price
        self.sell_price = sell_price
        self.availably = availably
        self.quantity = quantity



class Supply(Base):
    __tablename__ = 'supply'

    supply_id = Column(Integer(), primary_key=True)
    provider_id = Column(Integer(), ForeignKey('provider.provider_id', ondelete="CASCADE"))
    date_supply = Column(String(255))


    def __init__(self, supply_id, provider_id, date_supply):
        self.supply_id = supply_id
        self.provider_id = provider_id
        self.date_supply = date_supply


class Provider(Base):
    __tablename__ = 'provider'

    provider_id = Column(Integer(), primary_key=True)
    provider_name = Column(String(255))
    supplier_represent = Column(String(255))
    ask_to = Column(String(255))
    phone = Column(String(255))
    address = Column(String(255))

    def __init__(self, provider_id, provider_name, supplier_represent, ask_to, phone, address):
        self.provider_id = provider_id
        self.provider_name = provider_name
        self.supplier_represent = supplier_represent
        self.ask_to = ask_to
        self.phone = phone
        self.address = address


class Employee(Base):
    __tablename__ = 'employee'

    employee_id = Column(Integer(), primary_key=True)
    last_name = Column(String(255))
    first_name = Column(String(255))
    middle_name = Column(String(255))
    positions = Column(String(255))
    phone = Column(String(255))
    address = Column(String(255))
    birthday = Column(Date())

    def __init__(self, employee_id, last_name, first_name, middle_name, positions, phone, address, birthday):
        self.employee_id = employee_id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.positions = positions
        self.phone = phone
        self.address = address
        self.birthday = birthday


class Order(Base):
    __tablename__ = 'order'

    order_id = Column(Integer(), primary_key=True)
    employee_id = Column(Integer(), ForeignKey('employee.employee_id', ondelete="CASCADE"))
    good_id = Column(Integer(), ForeignKey('good.good_id', ondelete="CASCADE"))
    client_id = Column(Integer(), ForeignKey('client.client_id', ondelete="CASCADE"))
    positions = Column(String(255))
    phone = Column(String(255))
    address = Column(String(255))
    birthday = Column(Date())



    def __init__(self, order_id, employee_id, good_id, client_id, positions, phone, address, birthday):
        self.order_id = order_id
        self.employee_id = employee_id
        self.good_id = good_id
        self.client_id = client_id
        self.positions = positions
        self.phone = phone
        self.address = address
        self.birthday = birthday




#Base.metadata.create_all(engine)


c1 = Client(1, 'Ivanov Ivan Ivanovich', 'Moskwa Sovetskaya st 67-7', '123-87-43')
c2 = Client(2, 'Petrov Petr Petrovich', 'Kostroma Oktyabrya st 65-65', '234-76-43')
c3 = Client(3, 'Kozlov Ivan Sergeevich', 'Yaroslavl Sovetskaya st 78-87', '654-09-21')
c4 = Client(4, 'Ivanov Petr Ivanovich', 'Ivanovo Oktyabrya st 54-76', '567-87-43')
c5 = Client(5, 'Gerasimov Vasilii Ivanovich', 'Moskwa Oktyabrya st 9-5', '098-65-87')
c6 = Client(6, 'Soloviev Petr Aleksandrovich', "Kostroma Sovetskaya st 9-6", '345-87-87')

#session.bulk_save_objects([c1, c2, c3, c4, c5, c6])


p1 = Provider(1, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
p2 = Provider(2, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
p3 = Provider(3, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
p4 = Provider(4, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
p5 = Provider(5, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
p6 = Provider(6, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')

#session.bulk_save_objects([p1, p2, p3, p4, p5, p6])


s1 = Supply(1, 2, '1971-04-04')
s2 = Supply(2, 3, '1971-04-04')
s3 = Supply(3, 1, '1971-04-04')
s4 = Supply(4, 4, '1971-04-04')
s5 = Supply(5, 5, '1971-04-04')
s6 = Supply(6, 6, '1971-04-04')

#session.bulk_save_objects([s1, s2, s3, s4, s5, s6])

g1 = Good(1, 2, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', 1, 9, 1, 14)
g2 = Good(2, 3, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', 1, 9, 1, 14)
g3 = Good(3, 1, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', 1, 9, 1, 14)
g4 = Good(4, 4, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', 1, 9, 1, 14)
g5 = Good(5, 5, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', 1, 9, 1, 14)
g6 = Good(6, 6, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', 1, 9, 1, 14)

#session.bulk_save_objects([g1, g2, g3, g4, g5, g6])



e1 = Employee(1, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
e2 = Employee(2, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
e3 = Employee(3, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
e4 = Employee(4, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
e5 = Employee(5, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
e6 = Employee(6, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')

#session.bulk_save_objects([g1, g2, g3, g4, g5, g6])
#session.bulk_save_objects([e1, e2, e3, e4, e5, e6])



o1 = Order(1, 2, 3, 4, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
o2 = Order(2, 3, 4, 5, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
o3 = Order(3, 4, 5, 6, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
o4 = Order(4, 5, 6, 1, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
o5 = Order(5, 6, 1, 2, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')
o6 = Order(6, 1, 2, 3, '1971-04-04', '1971-04-04', '1971-04-04', '1971-04-04')



# Base.metadata.create_all(engine)
#
# session.bulk_save_objects([c1, c2, c3, c4, c5, c6])
# session.bulk_save_objects([p1, p2, p3, p4, p5, p6])
# session.bulk_save_objects([s1, s2, s3, s4, s5, s6])
# session.bulk_save_objects([g1, g2, g3, g4, g5, g6])
# session.bulk_save_objects([e1, e2, e3, e4, e5, e6])
# session.bulk_save_objects([o1, o2, o3, o4, o5, o6])

session.commit()



