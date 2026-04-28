# 🔍 Crimes Against Children in India — Data Analysis Project

A complete data analysis project on human trafficking cases reported across Indian states from 2001 to 2012, built using Python.

---

## 📁 Project Structure

```
crimes-analysis/
│
├── crimes.csv              # Raw dataset
├── crimes_analysis.py      # Main Python script
├── plot1_purpose.png       # Graph - Cases by Purpose
├── plot2_gender.png        # Graph - Gender Distribution
├── plot3_yeartrend.png     # Graph - Year-wise Trend
├── plot4_states.png        # Graph - Top 10 States
├── plot5_agegroup.png      # Graph - Age Group Distribution
└── README.md               # Project documentation
```

---

## 📊 Dataset Information

| Property | Details |
|----------|---------|
| Source | National Crime Records Bureau (NCRB), India |
| Years Covered | 2001 – 2012 |
| States Covered | 35 States and Union Territories |
| Total Rows | 5,866 |
| Total Columns | 19 |
| Total Victims | 3,61,459 |

### Columns in Dataset

- `STATE/UT` — Name of Indian state or union territory
- `YEAR` — Year of recorded cases
- `Pupose` — Purpose of trafficking (marriage, prostitution, begging, etc.)
- `Male/Female upto 10 years` — Victims aged 10 or below
- `Male/Female 10-15 years` — Victims aged 10 to 15
- `Male/Female 15-18 years` — Victims aged 15 to 18
- `Male/Female 18-30 years` — Victims aged 18 to 30
- `Male/Female 30-50 years` — Victims aged 30 to 50
- `Male/Female above 50 years` — Victims aged above 50
- `Total Male` — Total male victims
- `Total Female` — Total female victims
- `Grand Total` — Total victims (male + female)

---

## 🛠️ Libraries Used

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading, cleaning and analysis |
| `matplotlib` | Drawing charts and graphs |
| `seaborn` | Better looking visualisations |

Install all libraries using:

```bash
pip install pandas matplotlib seaborn
```

---

## ⚙️ How to Run

1. Clone this repository
```bash
git clone https://github.com/your-username/crimes-analysis.git
```

2. Place `crimes.csv` in the same folder as `crimes_analysis.py`

3. Update the file path in line 16 of the script:
```python
df = pd.read_csv(r"C:\your\path\to\crimes.csv")
```

4. Run the script:
```bash
python crimes_analysis.py
```

---

## 🧹 Data Cleaning Steps

- Checked and confirmed **no missing values**
- Checked and confirmed **no duplicate rows**
- Renamed column `Pupose` → `Purpose` (typo fix)
- Fixed value typo `"For unlawaful activity"` → `"For unlawful activity"`
- Removed aggregate `"Total"` rows to avoid double counting
- Stripped extra whitespace from state names and column headers

---

## 📈 Visualisations

### Graph 1 — Cases by Purpose
Horizontal bar chart showing which trafficking purpose had the most cases.
**Finding:** Marriage is the most common purpose with 1,65,838 cases.

### Graph 2 — Gender Distribution
Pie chart comparing total male vs female victims.
**Finding:** Female victims (73.5%) are nearly 3x more than male victims (26.5%).

### Graph 3 — Year-wise Trend
Line chart showing how total cases changed from 2001 to 2012.
**Finding:** Cases increased every year — nearly doubled from 23,000 to 48,000.

### Graph 4 — Top 10 States
Horizontal bar chart of the 10 states with highest reported cases.
**Finding:** Uttar Pradesh has the highest cases (59,347) followed by Bihar (37,259).

### Graph 5 — Age Group Distribution
Bar chart showing total victims across 6 age groups.
**Finding:** Age group 18–30 is the most affected with 2,03,534 victims.

---

## 🔑 Key Findings

1. **3,61,459 total victims** were recorded across India from 2001 to 2012
2. **Female victims are 3x more** than male victims — 73.5% vs 26.5%
3. **Marriage** is the biggest reason for trafficking — 45% of all cases
4. **Age group 18–30** has the most victims — over 56% of all cases
5. **Uttar Pradesh** leads all states in reported cases
6. Cases show a **steady rising trend** — nearly doubled over 12 years
7. **Selling body parts** is the rarest purpose with only 17 cases

---

## 📌 Project Workflow

```
Load Data  →  Data Cleaning  →  Feature Engineering  →  EDA  →  Visualisation
```


