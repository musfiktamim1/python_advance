import pandas as pd

df = pd.read_csv("20 Pandas/Datas/data.csv")

new_df = df.dropna()
print(df.info())
print(new_df.info())

df.dropna(inplace=True)
print(df.info())

