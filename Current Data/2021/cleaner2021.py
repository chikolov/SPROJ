import pandas as pd

print("Loading 2021 dataset...")

df = pd.read_csv("2021.csv")

# GPA columns
gpa_col = "C21B12"
scale_col = "C21B13"

# Convert to numeric
df[gpa_col] = pd.to_numeric(df[gpa_col], errors="coerce")
df[scale_col] = pd.to_numeric(df[scale_col], errors="coerce")

# Remove invalid NCES codes
invalid_codes = [0, 97, 98, 99, 997, 998, 999]

df = df[~df[gpa_col].isin(invalid_codes)]
df = df[~df[scale_col].isin(invalid_codes)]

# Keep valid GPA range
df = df[(df[gpa_col] > 0.01) & (df[gpa_col] <= 12)]
df = df[(df[scale_col] > 0.01) & (df[scale_col] <= 12)]

# Normalize GPA
df["GPA_normalized"] = df[gpa_col] / df[scale_col]

# Save cleaned dataset
df.to_csv("cleaned_2021.csv", index=False)

print("2021 dataset cleaned.")
print("Rows remaining:", len(df))