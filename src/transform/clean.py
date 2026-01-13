import pandas as pd

silver_path = "data/silver/Heart_Disease_Prediction_silver.csv"

def toSnakeCase(df):
    df.columns = df.columns.str.replace(" ", '_').str.lower()
    return df
    

def removeDuplicates(df):
    df = df.drop_duplicates()
    return df


# load data into a dataframe
df = pd.read_csv("data/bronze/Heart_Disease_Prediction.csv")

# Standardize data in the dataframe.
df_snake_case = toSnakeCase(df)

# remove duplicates from df
df_cleaned = removeDuplicates(df_snake_case)

# Save cleaned dataframe in silver folder
df_cleaned.to_csv(silver_path, index=False, sep=',', encoding='utf-8')
