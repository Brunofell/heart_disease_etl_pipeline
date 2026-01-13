from sqlalchemy import create_engine
import pandas as pd

# create conection with db
engine = create_engine("mysql+mysqlconnector://root:root@localhost:3307/heart_disease")

# path to csv in the silver folder
path_to_csv = "data/silver/Heart_Disease_Prediction_silver.csv"

# read data from silver
df = pd.read_csv(path_to_csv)

# load into mysql db
df.to_sql(
    name="heart_disease",
    con=engine,
    if_exists="append", # não recria se existir
    index=False
)

print("OK !!!! :)")