import pandas as pd

data = {
    "calories":[420,380,390],
    "duration":[50,40,45]
}

df = pd.DataFrame(data,index=["Day1","Day2","Day3"])
print(df)

print(df.loc["Day1"])
print(df.loc["Day2"])
print(df.loc["Day3"])
print(df.loc[["Day3","Day1"]])