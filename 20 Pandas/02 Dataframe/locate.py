import pandas as pd

data = {
    "calories":[420,380,390],
    "duration":[50,40,45]
}

df = pd.DataFrame(data)

print(df.loc[0]) #single row access
print(df.loc[[0,1]]) #multiple row access
