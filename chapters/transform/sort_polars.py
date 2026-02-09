# <transform_sort_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
#     "fsspec",
#     "requests",
# ]
# ///
import polars as pl
import io

# ---------------------------------------------------------
# Load Dataset (Palmer Penguins)
# ---------------------------------------------------------
URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

try:
    df = pl.read_csv(URL)
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
    df = pl.read_csv(io.StringIO(data))

print(f"Loaded {len(df)} rows.")

# ---------------------------------------------------------
# 1. Basic Sorting (Single Column)
# ---------------------------------------------------------
# Sort by bill length (descending)
# In Polars, use .sort() with `descending=True`
sorted_df = df.sort("bill_length_mm", descending=True)
print("\n--- Sort: bill_length_mm (Descending) ---")
print(sorted_df[["species", "bill_length_mm"]].head(3))

# ---------------------------------------------------------
# 2. Multi-Column Sorting
# ---------------------------------------------------------
# Sort by Island (A-Z), then by Body Mass (Heaviest first)
# Pass lists to both arguments
multi_sort = df.sort(
    ["island", "body_mass_g"], 
    descending=[False, True]
)
print("\n--- Sort: Island (ASC) then Body Mass (DESC) ---")
print(multi_sort[["island", "body_mass_g", "species"]].head(3))

# ---------------------------------------------------------
# 3. Top N Results (top_k efficient sort)
# ---------------------------------------------------------
# Get the 3 heaviest penguins efficiently
# The dataset might have nulls, top_k handles them
heaviest = df.top_k(3, by="body_mass_g")
print("\n--- Top 3 Heaviest Penguins (top_k) ---")
print(heaviest[["species", "body_mass_g"]])

# ---------------------------------------------------------
# 4. Null Handling
# ---------------------------------------------------------
# You can specify nulls_last=True explicitly if needed
# sorted_df = df.sort("bill_length_mm", descending=True, nulls_last=True)
# </transform_sort_polars>
