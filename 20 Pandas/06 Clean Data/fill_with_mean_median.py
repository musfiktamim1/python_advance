import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("20 Pandas/Datas/data.csv")
x = df["Calories"].mean()
df.fillna({"Calories":x},inplace=True)
print(df)


df = pd.read_csv("20 Pandas/Datas/data.csv")
x = df["Calories"].median()
df.fillna({"Calories":x},inplace=True)
print(df)

df = pd.read_csv("20 Pandas/Datas/data.csv")
x = df["Calories"].mode()[0]
df.fillna({"Calories":x},inplace=True)
print(df)

df.plot()
plt.show()