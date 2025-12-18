import pandas as pd

df = pd.read_csv("20 Pandas/Datas/data.csv")
new_df = df.fillna(130.0)
print(df.info())
print(new_df.info())

df = pd.read_csv("20 Pandas/Datas/data.csv")
df.fillna(130.0,inplace=True)
print(df.info())


df = pd.read_csv("20 Pandas/Datas/data.csv")
df.fillna({"Calories":130.0},inplace=True)
print(df.info())