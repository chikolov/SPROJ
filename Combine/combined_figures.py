import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "figure.figsize": (12, 6),
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10
})

PURPLE = "#6A0DAD"
LIGHT_PURPLE = "#C8A2C8"
COLOR_2014 = "#4B0082"
COLOR_2019 = "#6A0DAD"
COLOR_2021 = "#C8A2C8"
OUTPUT_DIR = "figures_final"


def find_file(filename):
    possible_paths = [
        filename,
        os.path.join("2014", filename),
        os.path.join("2019", filename),
        os.path.join("2021", filename),
        os.path.join("..", "2014", filename),
        os.path.join("..", "2019", filename),
        os.path.join("..", "2021", filename),
        os.path.join("..", filename)
    ]

    for path in possible_paths:
        if os.path.exists(path):
            return path

    raise FileNotFoundError(f"Could not find {filename}. Check the file path.")


def load_and_clean_2014():
    df = pd.read_csv(find_file("cleaned_2014.csv"))

    columns_to_keep = [
        "ER32000",
        "P14E5", "P14E6", "P14E15", "P14E16_3", "P14E53",
        "P14E10_09", "P14E26_5", "P14E33_6",
        "C14B12", "C14B13"
    ]

    df = df[columns_to_keep]

    df = df.rename(columns={
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
    })

    df["year"] = 2014
    return clean_gpa(df)


def load_and_clean_2019():
    df = pd.read_csv(find_file("cleaned_2019.csv"))

    columns_to_keep = [
        "ER32000",
        "P19E5", "P19E6", "P19E15", "P19E16_3", "P19E53A",
        "P19E10_09", "P19E26_5", "P19E33_6",
        "C19B12", "C19B13"
    ]

    df = df[columns_to_keep]

    df = df.rename(columns={
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
    })

    df["year"] = 2019
    return clean_gpa(df)


def load_and_clean_2021():
    df = pd.read_csv(find_file("cleaned_2021.csv"))

    columns_to_keep = [
        "ER32000",
        "P21E5", "P21E6", "P21E15", "P21E16_3", "P21E53A",
        "P21E10_09", "P21E26_5", "P21E33_6",
        "C21B12", "C21B13"
    ]

    df = df[columns_to_keep]

    df = df.rename(columns={
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
    })

    df["year"] = 2021
    return clean_gpa(df)


def clean_gpa(df):
    df = df.dropna(subset=["gpa_raw", "gpa_scale"])
    df = df[df["gpa_scale"] != 0]
    df["gpa_norm"] = df["gpa_raw"] / df["gpa_scale"]
    df = df[(df["gpa_norm"] >= 0) & (df["gpa_norm"] <= 1.0)]
    return df

def plot_ordinal_electronics(df2014, df2019, df2021):
    datasets = [df2014, df2019, df2021]
    years = ["2014", "2019", "2021"]
    colors = [COLOR_2014, COLOR_2019, COLOR_2021]

    categories = np.arange(1, 6)
    x = np.arange(len(categories))
    width = 0.25

    plt.figure(figsize=(10, 5))

    for i, df in enumerate(datasets):
        counts = (
            df["electronics_music"]
            .dropna()
            .astype(int)
            .value_counts()
            .reindex(categories, fill_value=0)
        )

        plt.bar(
            x + (i - 1) * width,
            counts.values,
            width,
            color=colors[i],
            label=years[i],
            edgecolor="black",
            alpha=0.85
        )

    plt.xticks(x, categories)
    plt.xlabel("Response Category")
    plt.ylabel("Frequency")
    plt.title("Distribution of Electronics Use for Listening to Music by Year")
    plt.legend(frameon=False)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "Figure_Ordinal_Electronics_Music.png"), dpi=300)
    plt.close()


def plot_ordinal_instruments(df2014, df2019, df2021):
    datasets = [df2014, df2019, df2021]
    years = ["2014", "2019", "2021"]
    colors = [COLOR_2014, COLOR_2019, COLOR_2021]

    categories = np.arange(1, 7)
    x = np.arange(len(categories))
    width = 0.25

    plt.figure(figsize=(10, 5))

    for i, df in enumerate(datasets):
        counts = (
            df["instrument_frequency"]
            .dropna()
            .astype(int)
            .value_counts()
            .reindex(categories, fill_value=0)
        )

        plt.bar(
            x + (i - 1) * width,
            counts.values,
            width,
            color=colors[i],
            label=years[i],
            edgecolor="black",
            alpha=0.85
        )

    plt.xticks(x, categories)
    plt.xlabel("Response Category")
    plt.ylabel("Frequency")
    plt.title("Distribution of Instrument Use Frequency by Year")
    plt.legend(frameon=False)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "Figure_Ordinal_Instrument_Frequency.png"), dpi=300)
    plt.close()

def plot_correlations_split(df2014, df2019, df2021):
    labels = {
        "music_lessons": "Music Lessons",
        "music_participation": "Music Participation",
        "instrument_home": "Instrument at Home",
        "arts_tutoring": "Arts Tutoring",
        "arts_community": "Arts Community Groups",
        "arts_religious": "Arts Religious Participation"
    }

    vars_ = list(labels.keys())

    corr_data = {}

    for var in vars_:
        corr14 = df2014[var].corr(df2014["gpa_norm"])
        corr19 = df2019[var].corr(df2019["gpa_norm"])
        corr21 = df2021[var].corr(df2021["gpa_norm"])

        corr_data[var] = [corr14, corr19, corr21]

    # Split by average sign across the three years
    negative_vars = [
        var for var in vars_
        if np.nanmean(corr_data[var]) < 0
    ]

    positive_vars = [
        var for var in vars_
        if np.nanmean(corr_data[var]) >= 0
    ]

    plot_correlation_group(
        corr_data,
        negative_vars,
        labels,
        "Negative Correlations Between Music/Arts Variables and GPA",
        "Figure_Correlations_Negative.png"
    )

    plot_correlation_group(
        corr_data,
        positive_vars,
        labels,
        "Positive Correlations Between Music/Arts Variables and GPA",
        "Figure_Correlations_Positive.png"
    )

def plot_correlation_group(corr_data, vars_, labels, title, filename):
    years = ["2014", "2019", "2021"]
    colors = [COLOR_2014, COLOR_2019, COLOR_2021]

    names = [labels[v] for v in vars_]
    x = np.arange(len(vars_))
    width = 0.25

    plt.figure(figsize=(10, 5))

    for i, year in enumerate(years):
        values = [corr_data[v][i] for v in vars_]

        plt.bar(
            x + (i - 1) * width,
            values,
            width,
            color=colors[i],
            label=year,
            edgecolor="black",
            alpha=0.85
        )

    plt.axhline(0, color="black", linewidth=1)

    plt.xticks(x, names, rotation=25, ha="right")
    plt.ylabel("Correlation with GPA")
    plt.title(title)
    plt.legend(frameon=False)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, filename), dpi=300)
    plt.close()

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df2014 = load_and_clean_2014()
    df2019 = load_and_clean_2019()
    df2021 = load_and_clean_2021()

    plot_ordinal_electronics(df2014, df2019, df2021)
    plot_ordinal_instruments(df2014, df2019, df2021)
    plot_correlations_split(df2014, df2019, df2021)


if __name__ == "__main__":
    main()