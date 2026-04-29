import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pointbiserialr, ttest_ind
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#load data
df = pd.read_csv("cleaned_2019.csv")

columns_to_keep = [
    'ER32000',
    'P19E5','P19E6','P19E15','P19E16_3','P19E53A',
    'P19E10_09','P19E26_5','P19E33_6',
    'C19B12','C19B13'
]

df = df[columns_to_keep]
df = df.dropna(subset=['C19B12','C19B13'])
df = df[df['C19B13'] != 0]
df["gpa_norm"] = df["C19B12"] / df["C19B13"]
df = df[df["gpa_norm"] <= 1.0]

df = df.rename(columns={
    'P19E15': 'music_lessons',
    'P19E16_3': 'music_participation',
    'P19E5': 'instrument_home',
    'P19E6': 'instrument_frequency',
    'P19E53A': 'electronics_music',
    'P19E10_09': 'arts_tutoring',
    'P19E26_5': 'arts_community',
    'P19E33_6': 'arts_religious'
})

labels = {
    "music_lessons": "Music Lessons",
    "music_participation": "Music Participation",
    "instrument_home": "Instrument at Home",
    "electronics_music": "Electronics for Music",
    "instrument_frequency": "Instrument use frequency",
    "arts_tutoring": "Arts Tutoring",
    "arts_community": "Arts Community Groups",
    "arts_religious": "Arts Religious"
}

binary_vars = [
    "music_lessons","music_participation","instrument_home",
    "arts_tutoring","arts_community","arts_religious"
]

ordinal_vars = ["electronics_music","instrument_frequency"]

gpa = df["gpa_norm"]

#gpa stats
print("\nGPA Statistics (2019)")
print("Count:", gpa.count())
print("Mean:", round(gpa.mean(),3))
print("Median:", round(gpa.median(),3))
print("Std:", round(gpa.std(),3))

plt.figure(figsize=(6,4))
plt.hist(gpa, bins=20, color="#6A0DAD", alpha=0.7)
plt.title("GPA Distribution (2019)")
plt.xlabel("Normalized GPA")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("figure_1.png")
plt.show()

#t tests
print("\nT-tests")

for col in binary_vars:
    temp = df[df[col].isin([1,5])]

    yes = temp[temp[col] == 1]["gpa_norm"]
    no  = temp[temp[col] == 5]["gpa_norm"]

    if len(yes) > 1 and len(no) > 1:
        t, pval = ttest_ind(yes, no)

        print(labels[col],": t =",round(t,3),"p =",round(pval,3))

        plt.figure(figsize=(6,4))
        plt.boxplot(
            [yes, no],
            tick_labels=["Yes","No"],
            widths=0.5,
            showfliers=True,
            boxprops=dict(linewidth=1.5),
            medianprops=dict(color='purple', linewidth=2)
        )
        plt.title(f"GPA vs {labels[col]} (2019)")
        plt.ylabel("Normalized GPA")
        plt.savefig(f"figure_{labels[col]}.png")
        plt.show()

#ordinal variables
for col in ordinal_vars:

    if col not in df.columns:
        continue

    print("\nFrequency:", labels.get(col, col))
    print(df[col].value_counts().sort_index())

    plt.figure(figsize=(6,4))

    if col == "electronics_music":
        bins = [0.5,1.5,2.5,3.5,4.5,5.5]
    elif col == "instrument_frequency":
        bins = [0.5,1.5,2.5,3.5,4.5,5.5,6.5]

    plt.hist(
        df[col].dropna(),
        bins=bins,
        color='purple',
        edgecolor='black',
        alpha=0.6
    )

    plt.title(f"Distribution of {labels.get(col, col)} (2019)")
    plt.xlabel("Response Category")
    plt.ylabel("Frequency")
    plt.savefig(f"figure_{col}.png")
    plt.show()

#correlations
corr_results = []

for var in binary_vars:
    valid = df[[var,"gpa_norm"]].dropna()
    r, p = pointbiserialr(valid[var], valid["gpa_norm"])
    corr_results.append([var, r, p])

corr_df = pd.DataFrame(corr_results, columns=["Variable","r_value","p_value"])
print("\nCorrelations:\n", corr_df)

plt.figure(figsize=(6,4))
plt.bar(corr_df["Variable"], corr_df["r_value"], color='purple')
plt.xticks(rotation=45)
plt.title("Point-Biserial Correlations with GPA (2019)")
plt.ylabel("Correlation (r)")
plt.tight_layout()
plt.savefig("figure_corr.png")
plt.show()

#regression
model_vars = [
    "music_lessons","music_participation","instrument_home",
    "instrument_frequency","electronics_music",
    "arts_tutoring","arts_community","arts_religious",
    "gpa_norm"
]

model_df = df[model_vars].dropna()

X = model_df.drop(columns=["gpa_norm"])
y = model_df["gpa_norm"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

#model performance
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("MAE:", round(mae,4))
print("RMSE:", round(rmse,4))
print("R²:", round(r2,4))

plt.figure(figsize=(6,4))
plt.scatter(
    y_test,
    y_pred,
    color='purple',
    alpha=0.75,
    s=80,
    edgecolors='black',
    linewidths=0.5
)
plt.plot([0,1], [0,1], color= "#C8A2C8", linestyle='-')
plt.xlabel("Actual GPA")
plt.ylabel("Predicted GPA")
plt.title("Actual vs Predicted GPA (2019)")
plt.savefig("figure_model.png")
plt.show()