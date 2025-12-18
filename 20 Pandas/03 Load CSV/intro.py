import pandas as pd

df = pd.read_csv("20 Pandas/Datas/data.csv")
print(df)
print(df.to_string())

print(pd.options.display.max_columns)
print(pd.options.display.max_rows)