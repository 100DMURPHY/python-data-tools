# <transform_pivot_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
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
    data = """species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
Adelie,Torgersen,39.1,18.7,181,3750,Male
Adelie,Torgersen,39.5,17.4,186,3800,Female
Adelie,Dream,40.3,18.0,195,3250,Female
Chinstrap,Dream,46.5,17.9,192,3500,Female
Gentoo,Biscoe,46.1,13.2,211,4500,Female
Gentoo,Biscoe,50.0,16.3,230,5700,Male
"""
    df = pl.read_csv(io.StringIO(data))

print(f"Loaded {len(df)} rows.")

# ---------------------------------------------------------
# 1. Pivot (Long → Wide)
# ---------------------------------------------------------
# Average body mass by species and island
pivot = df.pivot(
    on="island",
    index="species",
    values="body_mass_g",
    aggregate_function="mean"
)
print("\n--- Pivot: Avg Body Mass (Species x Island) ---")
print(pivot)

# ---------------------------------------------------------
# 2. Unpivot / Melt (Wide → Long)
# ---------------------------------------------------------
# First create a wide aggregated frame
wide_df = df.group_by("species").agg([
    pl.col("bill_length_mm").mean().alias("bill_length"),
    pl.col("bill_depth_mm").mean().alias("bill_depth")
])
print("\n--- Wide DataFrame ---")
print(wide_df)

# Unpivot (melt) to long format
long_df = wide_df.unpivot(
    on=["bill_length", "bill_depth"],
    index="species",
    variable_name="measurement",
    value_name="value"
)
print("\n--- Unpivoted (Long) DataFrame ---")
print(long_df)

# ---------------------------------------------------------
# 3. Transpose
# ---------------------------------------------------------
# Transpose switches rows and columns
transposed = wide_df.transpose(include_header=True, header_name="species")
print("\n--- Transposed ---")
print(transposed)
# </transform_pivot_polars>
