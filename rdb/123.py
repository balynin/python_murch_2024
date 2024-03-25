from sqlalchemy import create_engine

engine = create_engine(
    'postgresql+psycopg2://postgres:postgres@localhost/my_sales2',
    echo=True, pool_size=6, max_overflow=10
)
engine.connect()

print(engine)