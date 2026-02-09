import numpy as np
import pandas as pd

# aktivitas 1A
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv";
df = pd.read_csv(url);
print("Aktivitas 1A:");
print(df.shape);
print(df.head);

# aktivitas 1B
df.to_csv("titanic.csv", index=False)
df2 = pd.read_csv("titanic.csv")
print("Aktivitas 1B:");
print(df2.shape);
print(df2.head);

# aktivitas 2A
df.info()

num_cols = df.select_dtypes(include=["number"]).columns
cat_cols = df.select_dtypes(exclude=["number"]).columns
print(list (num_cols)[:5])
print(list (cat_cols)[:5])

# aktivitas 2B
print(num_cols)
print(cat_cols)
