from sqlalchemy import create_engine
import pandas as pd

# create conection with db
engine = create_engine("mysql+mysqlconnector://root:root@localhost:3307/heart_disease")

df = pd.read_sql("SELECT * FROM heart_disease", con=engine)

# creating numeric flag 
df["heart_disease_flag"] = df["heart_disease"].map({
    "Presence": 1,
    "Absence": 0
})

## groupBy -> one line for sex
## count -> total of pacients
## lambda x: (x == 1).sum() -> count how many have the disease

gold_df = (
    df.groupby("sex").agg( 
        total_pacients=("sex", "count"),
        total_with_disease=("heart_disease_flag", "sum")
    )
    .reset_index()
)

# creating the percentage % with disease
gold_df["percentage_with_disease"] = (gold_df["total_with_disease"] / gold_df["total_pacients"] * 100).round(2)

# is supposed to look like that 
# sex | total_pacients | total_with_disease | percentage_with_disease

# load into mysql db
gold_df.to_sql(
    name="heart_disease_by_sex",
    con=engine,
    if_exists="replace", # GOLD can be recalculated
    index=False
)

print("New heart_disease_by_sex table sucessfully created!")