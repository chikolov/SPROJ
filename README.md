
```markdown
# Quantitative Analysis of Music Education and Academic Performance (PSID-CDS)

<p align="center">
  <b>An empirical data science research project investigating the relationship between music education variables and children's academic performance using longitudinal panel data.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Domain-Data%20Science%20%2F%20Music%20Information%20Retrieval-blue" alt="Domain">
  <img src="https://img.shields.io/badge/Python-3.x-purple" alt="Python">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Status">
  <img src="https://img.shields.io/badge/Institution-Bard%20College-orange" alt="Institution">
</p>

---

## Executive Summary

This repository contains the code, data structures, and academic deliverables for my undergraduate senior thesis project at Bard College (B.S. in Computer Science & B.M. in Piano Performance). 

The project bridges computer science and behavioral research by utilizing automated data cleaning pipelines, multi-year longitudinal datasets, and statistical modeling to evaluate whether music education serves as an independent driver of academic success.

---

## Abstract

> Music education is frequently promoted as a way to improve children’s cognitive development and academic performance. However, prior research on the topic has produced mixed findings, often due to differences in methods used and the underlying role of socioeconomic status. This project examines the relationship between music education and academic performance using data from the Panel Study of Income Dynamics Child Development Supplement (PSID-CDS) for 2014, 2019, and 2021. After data cleaning and normalization, 1,173 students remained in the sample. Statistical methods included descriptive analysis, t-tests, correlations, regression, and predictive modeling.
>
> Results show that direct measures of music participation - taking lessons or general music involvement - were weak and inconsistent predictors of GPA. In contrast, having a musical instrument at home was the most stable and statistically significant predictor across all three years. The combined regression model explained 5.9% of the variance in GPA ($R^2 = 0.059$), suggesting that academic performance is influenced by factors beyond music variables. Predictive models also demonstrated limited explanatory power, reinforcing the complexity of academic performance.
>
> The findings suggest that music education contributes to student success indirectly, through broader factors like household and environmental influences, rather than as a strong independent cause of higher academic performance. This project supports previous findings that music education is a nuanced component of child development, rather than a standalone determinant of academic performance and outcomes.

---

## Repository Architecture

```text
senior_project/
│
├── data/                       # Multi-year longitudinal data directories
│   ├── 2014/                   # 2014 survey data, raw files, and documentation
│   ├── 2019/                   # 2019 survey data, raw files, and documentation
│   ├── 2021/                   # 2021 survey data, raw files, and documentation
│   └── combined/               # Cross-year merged analytical datasets
│
├── scripts/                    # Python data processing & modeling pipelines
│   ├── cleaner2014.py          # Data cleaning and normalization script
│   └── 2014.py                 # Statistical and regression analysis script
│
├── outputs/
│   └── figures_final/          # Final generated analytical plots and visualizations
│
├── docs/                       # Academic deliverables and presentation assets
│   ├── final_writing.pdf       # Complete senior thesis written report
│   ├── poster.pdf              # Final academic research presentation poster
│   └── logos/                 # Graphics and institutional logos
│
└── README.md                   # Project documentation

```

---

## Key Findings & Methodology

| Analytical Step | Tools & Techniques Used | Key Insights |
| --- | --- | --- |
| **Data Ingestion & Cleaning** | Pandas, NumPy, Custom Python Scripts | Harmonized and normalized multi-year survey data down to a validated cohort of **1,173 students** across 2014, 2019, and 2021. |
| **Exploratory Data Analysis** | Matplotlib, Seaborn, Correlation Matrices | Discovered that direct lesson participation yielded weak predictive power over GPA compared to environmental resource availability. |
| **Statistical Modeling** | SciPy, Statsmodels ($t$-tests, Regressions) | Built multi-variable regressions indicating **instrument accessibility at home** was the single most stable predictor across all years ($R^2 = 0.059$). |

---

## Tech Stack & Libraries

* **Language:** Python
* **Data Manipulation & Analysis:** `Pandas`, `NumPy`, `SciPy`, `Statsmodels`
* **Data Visualization:** `Matplotlib`, `Seaborn`
* **Data Source:** Panel Study of Income Dynamics Child Development Supplement (PSID-CDS)


```

```
