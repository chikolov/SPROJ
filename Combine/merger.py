import pandas as pd

data2014 = pd.read_csv("cleaned_2014.csv")
data2019 = pd.read_csv("cleaned_2019.csv")
data2021 = pd.read_csv("cleaned_2021.csv")

rename_2014 = {
    "ER32000": "sex",
    "P14E15": "music_lessons",
    "P14E16_3": "music_participation",
    "P14E5": "instrument_home",
    "P14E6": "instrument_frequency",
    "P14E53": "electronics_music",
    "P14E10_09": "arts_tutoring",
    "P14E26_5": "arts_community",
    "P14E33_6": "arts_religious",
    "C14B12": "gpa_raw",
    "C14B13": "gpa_scale"
}

rename_2019 = {
    "ER32000": "sex",
    "P19E15": "music_lessons",
    "P19E16_3": "music_participation",
    "P19E5": "instrument_home",
    "P19E6": "instrument_frequency",
    "P19E53A": "electronics_music",
    "P19E10_09": "arts_tutoring",
    "P19E26_5": "arts_community",
    "P19E33_6": "arts_religious",
    "C19B12": "gpa_raw",
    "C19B13": "gpa_scale"
}

rename_2021 = {
    "ER32000": "sex",
    "P21E15": "music_lessons",
    "P21E16_3": "music_participation",
    "P21E5": "instrument_home",
    "P21E6": "instrument_frequency",
    "P21E53A": "electronics_music",
    "P21E10_09": "arts_tutoring",
    "P21E26_5": "arts_community",
    "P21E33_6": "arts_religious",
    "C21B12": "gpa_raw",
    "C21B13": "gpa_scale"
}

data2014 = data2014.rename(columns=rename_2014)
data2019 = data2019.rename(columns=rename_2019)
data2021 = data2021.rename(columns=rename_2021)

data2014["year"] = 2014
data2019["year"] = 2019
data2021["year"] = 2021

for df in [data2014, data2019, data2021]:
    df["gpa_norm"] = df["gpa_raw"] / df["gpa_scale"]

columns = [
    "year",
    "sex",
    "music_lessons",
    "music_participation",
    "instrument_home",
    "instrument_frequency",
    "electronics_music",
    "arts_tutoring",
    "arts_community",
    "arts_religious",
    "gpa_norm"
]

data2014 = data2014[columns]
data2019 = data2019[columns]
data2021 = data2021[columns]

combined = pd.concat([data2014, data2019, data2021], ignore_index=True)
combined = combined.dropna(subset=["gpa_norm"])

combined.to_csv("combined_psid_music_data.csv", index=False)