# =========================================
# DATA ANALYSIS PROJECT (CLEAN + EDA + VIZ)
# =========================================

# -------- 1. IMPORT LIBRARIES --------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")
sns.set()

# -------- 2. LOAD DATA --------
df = pd.read_csv("C:/Users/aryak/Downloads/crimes.csv")

print("First 5 rows:\n", df.head())
print("\nShape:", df.shape)

# -------- 3. DATA CLEANING --------
print("\n--- DATA CLEANING ---")

df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)
df.columns = df.columns.str.strip()

print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# -------- 4. EDA --------
print("\n--- EDA ---")

print(df.describe())

total_cases = df.select_dtypes(include='number').sum().sum()
print("\nTotal Cases in Dataset:", total_cases)

# -------- GRAPH 1: HEATMAP --------
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# -------- GRAPH 2: YEAR-WISE TREND --------
yearly = df.groupby("YEAR")["Grand Total"].sum()

plt.figure(figsize=(10,5))
yearly.plot(marker='o')
plt.title("Year-wise Trend of Cases")
plt.xlabel("Year")
plt.ylabel("Cases")
plt.show()

# -------- 5. OBJECTIVES --------
print("\n--- OBJECTIVES ---")

# -------- GRAPH 3: PURPOSE --------
purpose_data = df.groupby("Pupose")["Grand Total"].sum().sort_values(ascending=False)

plt.figure(figsize=(12,6))
purpose_data.plot(kind='bar')
plt.title("Cases by Purpose")
plt.xlabel("Purpose")
plt.ylabel("Cases")
plt.xticks(rotation=45)
plt.show()

print("Most Common Purpose:", purpose_data.idxmax())

# -------- GRAPH 4: MALE vs FEMALE --------
male_total = df["Total Male"].sum()
female_total = df["Total Female"].sum()

plt.figure(figsize=(6,6))
plt.pie([male_total, female_total],
        labels=["Male", "Female"],
        autopct="%1.1f%%",
        startangle=90)
plt.title("Gender Distribution")
plt.show()

# -------- GRAPH 5: TOP 10 STATES --------
state_data = df.groupby("STATE/UT")["Grand Total"].sum()

top10 = state_data.sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top10.sort_values().plot(kind='barh')
plt.title("Top 10 States by Cases")
plt.xlabel("Cases")
plt.ylabel("States")
plt.show()

# -------- GRAPH 6: AGE GROUP --------
age_data = {
    "0-10": df["Male upto 10 years"].sum() + df["Female upto 10 years"].sum(),
    "10-15": df["Male 10-15 years"].sum() + df["Female 10-15 years"].sum(),
    "15-18": df["Male 15-18 years"].sum() + df["Female 15-18 years"].sum(),
    "18-30": df["Male 18-30 years"].sum() + df["Female 18-30 years"].sum(),
    "30-50": df["Male 30-50 years"].sum() + df["Female 30-50 years"].sum(),
    "50+": df["Male above 50 years"].sum() + df["Female above 50 years"].sum()
}

age_series = pd.Series(age_data)

plt.figure(figsize=(10,5))
age_series.plot(kind='bar')
plt.title("Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Cases")
plt.show()

print("Most Affected Age Group:", age_series.idxmax())

# -------- FINAL INSIGHTS --------
print("\n--- CONCLUSION ---")
print("1. Certain states contribute the highest number of cases.")
print("2. One gender is more affected than the other.")
print("3. Specific age groups are more vulnerable.")
print("4. Cases show variation across years.")
print("5. Some purposes dominate trafficking cases.")

print("\n✅ PROJECT COMPLETED SUCCESSFULLY")
