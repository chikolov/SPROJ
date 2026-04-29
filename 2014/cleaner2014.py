import pandas as pd

df = pd.read_csv("2014.csv")

df["C14B12"] = pd.to_numeric(df["C14B12"], errors="coerce")
df["C14B13"] = pd.to_numeric(df["C14B13"], errors="coerce")

df = df[(df["C14B12"] > 0.01) & (df["C14B12"] <= 12)]
df = df[(df["C14B13"] > 0.01) & (df["C14B13"] <= 12)]

df["GPA_normalized"] = df["C14B12"] / df["C14B13"]

df.to_csv("cleaned_2014.csv", index=False)