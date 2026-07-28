import pandas as pd
import statsmodels.api as sm

# Load combined dataset
data = pd.read_csv("combined_psid_music_data.csv")
df2014 = data[data["year"] == 2014].copy()
df2019 = data[data["year"] == 2019].copy()
df2021 = data[data["year"] == 2021].copy()

variables = [
    "music_lessons",
    "music_participation",
    "instrument_home",
    "instrument_frequency",
    "electronics_music",
    "arts_tutoring",
    "arts_community",
    "arts_religious",
    "year",
    "gpa_norm"
]

print("\nCOMBINED DATASET SUMMARY")

print("\nGPA Stats:")
print("Count:", data["gpa_norm"].count())
print("Mean:", round(data["gpa_norm"].mean(),3))
print("Median:", round(data["gpa_norm"].median(),3))
print("Std:", round(data["gpa_norm"].std(),3))
print("\nObservations by Year:")
print(data["year"].value_counts().sort_index)
      
# remove rows with missing values
data = data[variables].dropna()

X = data.drop(columns=["gpa_norm"])
y = data["gpa_norm"]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())
