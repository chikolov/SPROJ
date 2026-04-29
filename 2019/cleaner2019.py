import pandas as pd

print("Loading 2019 dataset...")

df = pd.read_csv("2019.csv")

gpa_col = "C19B12"
scale_col = "C19B13"

df[gpa_col] = pd.to_numeric(df[gpa_col], errors="coerce")
df[scale_col] = pd.to_numeric(df[scale_col], errors="coerce")
invalid_codes = [0, 97, 98, 99, 997, 998, 999]

df = df[~df[gpa_col].isin(invalid_codes)]
df = df[~df[scale_col].isin(invalid_codes)]
df = df[(df[gpa_col] > 0.01) & (df[gpa_col] <= 12)]
df = df[(df[scale_col] > 0.01) & (df[scale_col] <= 12)]

df["GPA_normalized"] = df[gpa_col] / df[scale_col]
df.to_csv("cleaned_2019.csv", index=False)