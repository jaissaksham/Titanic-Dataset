import pandas as pd

df = pd.read_csv("Titanic-Dataset - Titanic-Dataset (2).csv")

print(df.head())
print(df.info())
print(df.isnull().sum())