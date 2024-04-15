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

