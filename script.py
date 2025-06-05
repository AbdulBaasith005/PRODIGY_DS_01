import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

age_groups = ["0-4 years", "5-14 years", "15-24 years", "25-64 years", "65+"]

age_totals = df[age_groups].sum()

age_totals_billion = age_totals / 1e9

plt.figure(figsize=(8, 5))
bars = plt.bar(age_totals_billion.index, age_totals_billion.values, color='lightblue')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f"{height:.2f}B", ha='center', va='bottom')

plt.title("Total Population by Age Group (in Billions)")
plt.xlabel("Age Group")
plt.ylabel("Population (Billions)")
plt.tight_layout()

plt.show()
