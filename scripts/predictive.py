from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

data = data[data["gpa_norm"] <= 1.0]
X = data.drop(columns=["gpa_norm"])
y = data["gpa_norm"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model_pred = LinearRegression()
model_pred.fit(X_train, y_train)
y_pred = model_pred.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nPredictive Model Performance (Combined Data):")
print("MAE:", round(mae,4))
print("RMSE:", round(rmse,4))
print("R²:", round(r2,4))

plt.figure(figsize=(6,4))
plt.scatter(y_test, y_pred, color='purple', alpha=0.75, s=80, edgecolors='black', linewidths=0.5)
plt.plot([0,1], [0,1], color="#C8A2C8", linestyle='-')
plt.xlabel("Actual GPA")
plt.ylabel("Predicted GPA")
plt.title("Actual vs Predicted GPA (Combined)")
plt.savefig("combined_model.png")
plt.show()
