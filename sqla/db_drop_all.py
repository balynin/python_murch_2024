from db_init import *

Base.metadata.drop_all(engine)
session.commit()
