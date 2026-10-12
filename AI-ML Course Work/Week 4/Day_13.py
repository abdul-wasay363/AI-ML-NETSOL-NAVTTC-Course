from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. LOAD RAW DATASET & INITIAL INSPECTION
data_path = Path(__file__).parent / "pakistan house prediction dataset.csv"
df_raw = pd.read_csv(data_path)

print("=" * 80)
print("1. RAW DATASET OVERVIEW")
print("=" * 80)
print(f"Dataset Shape: {df_raw.shape[0]} rows, {df_raw.shape[1]} columns")
print("\nFirst 5 rows:")
print(df_raw.head())
print("\nData Types & Non-Null Counts:")
df_raw.info()

print("\nMissing Values per column:")
missing_raw = df_raw.isnull().sum()
missing_pct = (missing_raw / len(df_raw)) * 100
missing_df = pd.DataFrame(
    {"Missing Count": missing_raw, "Percentage (%)": missing_pct.round(2)}
)
print(missing_df[missing_df["Missing Count"] > 0])

# Duplicate Checks
duplicate_rows = df_raw.duplicated().sum()
duplicate_ids = df_raw.duplicated(subset=["ID"]).sum()
print(f"\nExact duplicate rows: {duplicate_rows}")
print(f"Duplicate IDs: {duplicate_ids}")

# 2. DATA CLEANING & STANDARDIZATION
print("\n" + "=" * 80)
print("2. DATA CLEANING & PREPROCESSING")
print("=" * 80)

df = df_raw.copy()

# Step A: Drop duplicate rows based on ID
df = df.drop_duplicates(subset=["ID"]).reset_index(drop=True)
print(f"Rows after removing duplicate IDs: {len(df)}")

# Step B: Clean Area_SqFt (remove 'sqft', 'Sq. Ft.', commas, spaces, 'N/A')
df["Area_SqFt"] = df["Area_SqFt"].astype(str).str.replace(r"[^\d.]", "", regex=True)
df["Area_SqFt"] = pd.to_numeric(df["Area_SqFt"], errors="coerce")

# Step C: Clean Price_PKR (remove commas, currency symbols, spaces)
df["Price_PKR"] = df["Price_PKR"].astype(str).str.replace(r"[^\d.]", "", regex=True)
df["Price_PKR"] = pd.to_numeric(df["Price_PKR"], errors="coerce")

# Step D: Clean Year_Built
df["Year_Built"] = df["Year_Built"].astype(str).str.replace(r"[^\d.]", "", regex=True)
df["Year_Built"] = pd.to_numeric(df["Year_Built"], errors="coerce")

# Step E: Clean numeric columns (Bedrooms, Bathrooms, Floors, Garage)
for col in ["Bedrooms", "Bathrooms", "Floors", "Garage"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Step F: Standardize Text/Categorical Columns
text_cols = ["City", "Location", "Condition", "Property_Type"]
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()
    # Replace 'Nan', 'N/A' strings with actual NaN
    df[col] = df[col].replace({"Nan": np.nan, "N/A": np.nan, "Na": np.nan, "": np.nan})

# Standardize Binary Flags (Furnished, Corner_Property, Park_Facing)
binary_cols = ["Furnished", "Corner_Property", "Park_Facing"]
for col in binary_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .str.title()
        .replace({"Nan": np.nan, "N/A": np.nan, "Na": np.nan, "": np.nan})
    )

print("Sample cleaned records:")
print(df[["ID", "Area_SqFt", "Price_PKR", "Year_Built", "City", "Condition"]].head())

# 3. FEATURE ENGINEERING
print("\n" + "=" * 80)
print("3. FEATURE ENGINEERING")
print("=" * 80)

# A. Convert Area to Marla (Housing society standard: 1 Marla = 225 sq ft)
SQFT_PER_MARLA = 225
df["Area_Marla"] = df["Area_SqFt"] / SQFT_PER_MARLA

# B. Convert Price to Crores (1 Crore = 10,000,000 PKR) & Lakhs (1 Lakh = 100,000 PKR)
df["Price_Crores"] = df["Price_PKR"] / 10_000_000
df["Price_Lakhs"] = df["Price_PKR"] / 100_000

# C. Price per Marla & Price per SqFt (in Lakhs)
df["Price_Per_Marla_Lakhs"] = df["Price_Lakhs"] / df["Area_Marla"]
df["Price_Per_SqFt_PKR"] = df["Price_PKR"] / df["Area_SqFt"]

# D. House Age (current year 2026 - Year_Built)
CURRENT_YEAR = 2026
df["House_Age"] = CURRENT_YEAR - df["Year_Built"]

print("Engineered Features Sample:")
print(
    df[
        [
            "Area_SqFt",
            "Area_Marla",
            "Price_Crores",
            "Price_Per_Marla_Lakhs",
            "House_Age",
        ]
    ].head()
)

# 4. OUTLIER & ANOMALY DETECTION
print("\n" + "=" * 80)
print("4. ANOMALY & OUTLIER DETECTION")
print("=" * 80)

# Detect Extreme Price Outliers (e.g. 5 Billion / 10 Billion PKR)
extreme_high_prices = df[df["Price_PKR"] >= 500_000_000]
print(f"Houses with Price >= 50 Crore (500M PKR): {len(extreme_high_prices)}")
if len(extreme_high_prices) > 0:
    print(
        extreme_high_prices[
            ["ID", "Area_SqFt", "Area_Marla", "Price_PKR", "Price_Crores", "City"]
        ]
    )

# Detect Extreme Low Prices (e.g. 1 Lakh for a large house)
extreme_low_prices = df[df["Price_PKR"] < 1_000_000]
print(f"\nHouses with Price < 10 Lakh (1M PKR): {len(extreme_low_prices)}")
if len(extreme_low_prices) > 0:
    print(extreme_low_prices[["ID", "Area_SqFt", "Area_Marla", "Price_PKR", "City"]])

# Detect Zero or Tiny Areas (< 100 sq ft)
tiny_area = df[df["Area_SqFt"] < 100]
print(f"\nHouses with Area < 100 SqFt: {len(tiny_area)}")
if len(tiny_area) > 0:
    print(tiny_area[["ID", "Area_SqFt", "Area_Marla", "Price_PKR", "City"]])

# Create a Realistic Subset (filtered of extreme synthetic artifacts) for truthful statistics:
# Realistic bounds: Area between 100 sq ft and 15,000 sq ft, Price between 10 Lakh and 40 Crore (400M)
valid_mask = df["Area_SqFt"].between(100, 15_000) & df["Price_PKR"].between(
    1_000_000, 400_000_000
)
df_valid = df[valid_mask].copy()
print(
    f"\nRealistic Clean Dataset size (excluding anomalies): {len(df_valid)} valid houses"
)

# Save preprocessed data in the same folder as your Python script
output_path = Path(__file__).parent / "pakistan_house_preprocessed.csv"

df_valid.to_csv(output_path, index=False)

print(f"Preprocessed dataset saved to: {output_path}")

# ==============================================================================
# 5. UNIVARIATE ANALYSIS (DISTRIBUTIONS & SUMMARY STATS)
# ==============================================================================
print("\n" + "=" * 80)
print("5. UNIVARIATE ANALYSIS (REALISTIC DATASET)")
print("=" * 80)

num_cols = [
    "Area_SqFt",
    "Area_Marla",
    "Price_PKR",
    "Price_Crores",
    "Bedrooms",
    "Bathrooms",
    "Floors",
    "House_Age",
]
print("Numerical Features Summary:")
print(df_valid[num_cols].describe().round(2).T)

print("\nCategorical Distributions:")
print("\n--- Distribution by City ---")
print(df_valid["City"].value_counts(dropna=False))

print("\n--- Distribution by Condition ---")
print(df_valid["Condition"].value_counts(dropna=False))

print("\n--- Distribution by Property Type ---")
print(df_valid["Property_Type"].value_counts(dropna=False))

print("\n--- Distribution by Furnished ---")
print(df_valid["Furnished"].value_counts(dropna=False))

# 6. BIVARIATE & MULTIVARIATE ANALYSIS
print("\n" + "=" * 80)
print("6. BIVARIATE ANALYSIS & RELATIONSHIPS")
print("=" * 80)

# A. Average Price by City
city_stats = (
    df_valid.groupby("City")
    .agg(
        Avg_Price_Crores=("Price_Crores", "mean"),
        Median_Price_Crores=("Price_Crores", "median"),
        Avg_Area_Marla=("Area_Marla", "mean"),
        Total_Listings=("Price_Crores", "count"),
    )
    .round(2)
    .sort_values("Avg_Price_Crores", ascending=False)
)
print("City-wise Real Estate Summary:")
print(city_stats)

# B. Average Price by Condition
condition_stats = (
    df_valid.groupby("Condition")
    .agg(
        Avg_Price_Crores=("Price_Crores", "mean"),
        Median_Price_Crores=("Price_Crores", "median"),
        Count=("Price_Crores", "count"),
    )
    .round(2)
    .sort_values("Avg_Price_Crores", ascending=False)
)
print("\nCondition-wise Price Summary:")
print(condition_stats)

# C. Value addition of Amenities (Corner, Park Facing, Furnished)
print("\nAmenity Premiums (Mean Price in Crores):")
for amenity in ["Furnished", "Corner_Property", "Park_Facing"]:
    premium = df_valid.groupby(amenity)["Price_Crores"].mean().round(2)
    print(f"\n{amenity}:")
    print(premium)

# D. Pearson Correlation Matrix
corr_cols = [
    "Price_Crores",
    "Area_Marla",
    "Bedrooms",
    "Bathrooms",
    "Floors",
    "Year_Built",
    "House_Age",
]
corr_matrix = df_valid[corr_cols].corr()
print("\nCorrelation Matrix with Price_Crores:")
print(corr_matrix["Price_Crores"].sort_values(ascending=False).round(4))