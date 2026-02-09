# <transform_pivot_pandas>
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
    data = """species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
Adelie,Torgersen,39.1,18.7,181,3750,Male
Adelie,Torgersen,39.5,17.4,186,3800,Female
Adelie,Dream,40.3,18.0,195,3250,Female
Chinstrap,Dream,46.5,17.9,192,3500,Female
Gentoo,Biscoe,46.1,13.2,211,4500,Female
Gentoo,Biscoe,50.0,16.3,230,5700,Male
"""
    df = pd.read_csv(io.StringIO(data))

print(f"Loaded {len(df)} rows.")

# ---------------------------------------------------------
# 1. Pivot Table (Long → Wide)
# ---------------------------------------------------------
# Create a summary: average body mass by species and island
pivot = df.pivot_table(
    values='body_mass_g',
    index='species',
    columns='island',
    aggfunc='mean'
)
print("\n--- Pivot Table: Avg Body Mass (Species x Island) ---")
print(pivot.round(0))

# ---------------------------------------------------------
# 2. Melt (Wide → Long)
# ---------------------------------------------------------
# First create a wide dataframe
wide_df = df.groupby('species')[['bill_length_mm', 'bill_depth_mm']].mean().reset_index()
print("\n--- Wide DataFrame ---")
print(wide_df.round(1))

# Now melt it back to long format
long_df = wide_df.melt(
    id_vars=['species'],
    value_vars=['bill_length_mm', 'bill_depth_mm'],
    var_name='measurement',
    value_name='value'
)
print("\n--- Melted (Long) DataFrame ---")
print(long_df.round(1))

# ---------------------------------------------------------
# 3. Stack / Unstack
# ---------------------------------------------------------
# Multi-index example
multi_idx = df.groupby(['species', 'island'])['body_mass_g'].mean()
print("\n--- Multi-Index Series (Stacked) ---")
print(multi_idx.head(6).round(0))

# Unstack to make it wide
unstacked = multi_idx.unstack()
print("\n--- Unstacked (Wide) ---")
print(unstacked.round(0))
# </transform_pivot_pandas>
