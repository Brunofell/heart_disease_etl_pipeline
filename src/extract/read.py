import pandas as pd

df = pd.read_csv("data/bronze/Heart_Disease_Prediction.csv")

print(">> Visualization: ")
print(df.head())

print(">> informations: ")
df.info()

print(">> Type: ")
print(type(df))

print(">> Columns number: ")
print(df.shape[1])