# <transform_sort_pandas>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
# ]
# ///
import pandas as pd
import io

# ---------------------------------------------------------
# Load Dataset (Palmer Penguins)
# ---------------------------------------------------------
URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

try:
    df = pd.read_csv(URL)
except Exception:
    print("Warning: Failed to load data from URL. Mocking data.")
    data = """species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
Adelie,Torgersen,39.1,18.7,181,3750,Male
Adelie,Torgersen,39.5,17.4,186,3800,Female
Adelie,Torgersen,40.3,18.0,195,3250,Female
Adelie,Torgersen,36.7,19.3,193,3450,Female
Adelie,Torgersen,39.3,20.6,190,3650,Male
Chinstrap,Dream,46.5,17.9,192,3500,Female
Chinstrap,Dream,50.0,19.5,196,3900,Male
Gentoo,Biscoe,46.1,13.2,211,4500,Female
Gentoo,Biscoe,50.0,16.3,230,5700,Male
"""
    df = pd.read_csv(io.StringIO(data))

print(f"Loaded {len(df)} rows.")

# ---------------------------------------------------------
# 1. Basic Sorting (Single Column)
# ---------------------------------------------------------
# Sort by bill length (descending) - longest bills first
sorted_df = df.sort_values(by="bill_length_mm", ascending=False)
print("\n--- Sort: bill_length_mm (Descending) ---")
print(sorted_df[["species", "bill_length_mm"]].head(3))

# ---------------------------------------------------------
# 2. Multi-Column Sorting
# ---------------------------------------------------------
# Sort by Island (A-Z), then by Body Mass (Heaviest first)
multi_sort = df.sort_values(
    by=["island", "body_mass_g"], 
    ascending=[True, False]
)
print("\n--- Sort: Island (ASC) then Body Mass (DESC) ---")
print(multi_sort[["island", "body_mass_g", "species"]].head(3))

# ---------------------------------------------------------
# 3. Top N Results (nlargest)
# ---------------------------------------------------------
# Get the 3 heaviest penguins
heaviest = df.nlargest(3, "body_mass_g")
print("\n--- Top 3 Heaviest Penguins ---")
print(heaviest[["species", "body_mass_g"]])

# ---------------------------------------------------------
# 4. Sorting by Index
# ---------------------------------------------------------
# Sometimes you want to return to original order or sort by index
sorted_by_index = df.sort_index()
print("\n--- Sort by Index ---")
print(sorted_by_index.head(3))
# </transform_sort_pandas>
