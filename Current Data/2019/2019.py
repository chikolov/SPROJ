import pandas as pd
import pylab as p
from scipy.stats import pointbiserialr, ttest_ind

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

df["GPA_normalized"] = df["C19B12"] / df["C19B13"]

labels = {
"P19E5": "Instrument at Home",
"P19E6": "Instrument Use Frequency",
"P19E15": "Music Lessons",
"P19E16_3": "Music Lesson Participation",
"P19E53A": "Electronics for Music",
"P19E10_09": "Arts Tutoring",
"P19E26_5": "Arts Community Groups",
"P19E33_6": "Arts Religious Performance"
}

binary_vars = [
'P19E15','P19E16_3','P19E5','P19E10_09','P19E26_5','P19E33_6'
]

ordinal_vars = ['P19E53A','P19E6']

gpa = df['GPA_normalized']

print("\nGPA Statistics (2019)")
print("Count:",gpa.count())
print("Mean:",round(gpa.mean(),3))
print("Median:",round(gpa.median(),3))
print("Std:",round(gpa.std(),3))

p.figure(figsize=(6,4))
p.hist(gpa.dropna(), bins=20, color='purple', edgecolor='black', alpha=0.6)
p.title("GPA Distribution (2019)")
p.xlabel("Normalized GPA")
p.ylabel("Frequency")
p.show()

print("\nT-tests")

for col in binary_vars:

    temp = df[df[col].isin([1,5])]
    yes = temp[temp[col]==1]['GPA_normalized']
    no  = temp[temp[col]==5]['GPA_normalized']

    if len(yes)>1 and len(no)>1:

        t,pval = ttest_ind(yes,no)

        print(labels[col],": t =",round(t,3),"p =",round(pval,3))

        p.figure(figsize=(6,4))
        p.boxplot([yes,no],tick_labels=["Yes","No"], 
            showfliers=True,
            widths=0.5,
            boxprops=dict(linewidth=1.5),
            medianprops=dict(color='purple', linewidth=2)
)
        p.title(f"GPA vs {labels[col]} (2019)")
        p.ylabel("Normalized GPA")
        p.show()
print("\nOrdinal Variable Frequencies")

for col in ordinal_vars:

    clean = df[col].dropna()

    clean = clean[clean > 0]

    print("\nFrequency:",labels[col])
    print(clean.value_counts().sort_index())

    p.figure(figsize=(6,4))
    p.hist(df[col].dropna(),bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5], color='purple', edgecolor='black', alpha=0.6)
    p.title(f"Distribution of {labels[col]} (2019)")
    p.xlabel("Response Category")
    p.ylabel("Frequency")
    p.show()

print("\nPoint-Biserial Correlations")

for col in binary_vars:

    valid = df[[col,'GPA_normalized']].dropna()

    r,pval = pointbiserialr(valid[col],valid['GPA_normalized'])

    print(labels[col],"→ r =",round(r,3),"p =",round(pval,3))