import pandas as pd
import pylab as p
from scipy.stats import pointbiserialr, ttest_ind

# ======================
# LOAD DATA
# ======================

df = pd.read_csv("cleaned_2014.csv")

columns_to_keep = [
    'ER32000',
    'P14E5',
    'P14E6',
    'P14E15',
    'P14E16_3',
    'P14E53',
    'P14E10_09',
    'P14E26_5',
    'P14E33_6',
    'C14B12',
    'C14B13'
]

df = df[columns_to_keep]

# ======================
# CLEAN DATA
# ======================

df = df.dropna(subset=['C14B12','C14B13'])
df = df[df['C14B13'] != 0]

df["GPA_normalized"] = df["C14B12"] / df["C14B13"]

# ======================
# LABELS
# ======================

labels = {
"P14E5": "Instrument at Home",
"P14E6": "Instrument Use Frequency",
"P14E15": "Music Lessons",
"P14E16_3": "Music Lesson Participation",
"P14E53": "Electronics for Music/TV",
"P14E10_09": "Arts Tutoring",
"P14E26_5": "Arts Community Groups",
"P14E33_6": "Arts Religious Performance",
"ER32000": "Sex"
}

binary_vars = [
'P14E15','P14E16_3','P14E5','P14E10_09','P14E26_5','P14E33_6'
]

ordinal_vars = ['P14E53']
ordinal_single = ['P14E6']

gpa = df['GPA_normalized']

# ======================
# GPA STATS
# ======================

print("\nGPA Statistics (2014)")
print("Count:", gpa.count())
print("Mean:", round(gpa.mean(),3))
print("Median:", round(gpa.median(),3))
print("Std:", round(gpa.std(),3))

# ======================
# HISTOGRAM
# ======================

p.figure(figsize=(6,4))
p.hist(gpa.dropna(), bins=20, color='purple', edgecolor='black', alpha=0.6)
p.title("GPA Distribution (2014)")
p.xlabel("Normalized GPA")
p.ylabel("Frequency")
p.show()

# ======================
# T TESTS
# ======================

print("\nT-tests")

for col in binary_vars:

    temp = df[df[col].isin([1,5])]

    yes = temp[temp[col] == 1]['GPA_normalized']
    no  = temp[temp[col] == 5]['GPA_normalized']

    if len(yes) > 1 and len(no) > 1:

        t,pval = ttest_ind(yes,no)

        print(labels[col],": t =",round(t,3),"p =",round(pval,3))

        p.figure(figsize=(6,4))
        p.boxplot([yes,no],tick_labels=["Yes","No"], 
            showfliers=True,
            widths=0.5,
            boxprops=dict(linewidth=1.5),
            medianprops=dict(color='purple', linewidth=2)
)
        p.title(f"GPA vs {labels[col]} (2014)")
        p.ylabel("Normalized GPA")
        p.show()

# ======================
# ORDINAL DISTRIBUTIONS
# ======================

for col in ordinal_vars:

    print("\nFrequency:",labels[col])
    print(df[col].value_counts().sort_index())

    p.figure(figsize=(6,4))
    p.hist(df[col].dropna(),bins=[0.5,1.5,2.5,3.5,4.5,5.5], color='purple', edgecolor='black', alpha=0.6)
    p.title(f"Distribution of {labels[col]} (2014)")
    p.xlabel("Response Category")
    p.ylabel("Frequency")
    p.show()

for col in ordinal_single:

    print("\nFrequency:",labels[col])
    print(df[col].value_counts().sort_index())

    p.figure(figsize=(6,4))
    p.hist(df[col].dropna(),bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], color='purple', edgecolor='black', alpha=0.6)
    p.title(f"Distribution of {labels[col]}")
    p.xlabel("Response Category")
    p.ylabel("Frequency")
    p.show()

# ======================
# CORRELATIONS
# ======================

print("\nPoint-Biserial Correlations")

for col in binary_vars:

    valid = df[[col,'GPA_normalized']].dropna()

    r,pval = pointbiserialr(valid[col],valid['GPA_normalized'])

    print(labels[col],"→ r =",round(r,3),"p =",round(pval,3))