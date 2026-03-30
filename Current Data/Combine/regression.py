import pandas as pd
import statsmodels.api as sm

# Load combined dataset
data = pd.read_csv("combined_psid_music_data.csv")

# Variables used in regression
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

# Remove rows with missing values in ANY variable used
data = data[variables].dropna()

print("Sample size after cleaning:", len(data))

# Define X and y
X = data.drop(columns=["gpa_norm"])
y = data["gpa_norm"]

# Add constant
X = sm.add_constant(X)

# Run regression
model = sm.OLS(y, X).fit()

print(model.summary())