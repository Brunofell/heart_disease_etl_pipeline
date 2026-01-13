from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:root@localhost:3307/heart_disease")

with engine.connect() as conn:
    print("OK!!!!")