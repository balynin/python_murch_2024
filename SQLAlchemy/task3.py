from sqlalchemy import create_engine, insert

engine = create_engine(
    'postgresql+psycopg2://postgres:postgres@localhost/my_sales2',
    #'sqlite:///:memory:',
    echo=True, pool_size=6, max_overflow=10
)

from sqlalchemy import MetaData, Table, Column, Integer, String, Text, ForeignKey, Boolean, Date

metadata = MetaData()

client = Table('client', metadata,
    Column('client_id', Integer(), primary_key=True),
    Column('fio', Text()),
    Column('address', Text()),
    Column('phone', Text()),
)

good = Table('good', metadata,
    Column('good_id', Integer(), primary_key=True),
    Column('supply_id',  ForeignKey("supply.supply_id")),
    Column('good_name', Text()),
    Column('specifications', Text()),
    Column('description', Text()),
    Column('pic', Text()),
    Column('cost_price', Integer()),
    Column('sell_price', Integer()),
    Column('availably', Boolean()),
    Column('quantity', Integer()),
)

supply = Table('supply', metadata,
    Column('supply_id', Integer(), primary_key=True),
    Column('provider_id', ForeignKey("provider.provider_id")),
    Column('date_supply', Date()),
)

provider = Table('provider', metadata,
    Column('provider_id', Integer(), primary_key=True),
    Column('provider_name', Text()),
    Column('supplier_represent', Text()),
    Column('ask_to', Text()),
    Column('phone', Text()),
    Column('address', Text()),
)

employee = Table('employee', metadata,
    Column('employee_id', Integer(), primary_key=True),
    Column('last_name', Text()),
    Column('first_name', Text()),
    Column('middle_name', Text()),
    Column('positions', Text()),
    Column('phone', Text()),
    Column('address', Text()),
    Column('birthday', Date()),
)

order = Table('order', metadata,
    Column('order_id', Integer(), primary_key=True),
    Column('employee_id', ForeignKey('employee.employee_id')),
    Column('good_id', ForeignKey('good.good_id')),
    Column('client_id', ForeignKey('client.client_id')),
    Column('positions', Text()),
    Column('phone', Text()),
    Column('address', Text()),
    Column('birthday', Date()),
)


metadata.create_all(engine)
metadata.drop_all(engine)

