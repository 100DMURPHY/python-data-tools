# <transform_window_polars>
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

# Clean up for demo
df = df.drop_nulls(subset=["body_mass_g"]).head(20)
print(f"Using {len(df)} rows for demo.")

# ---------------------------------------------------------
# 1. RANK: Ranking within Groups
# ---------------------------------------------------------
# Polars uses .over() for window functions
result = df.with_columns(
    pl.col("body_mass_g")
    .rank(method="dense", descending=True)
    .over("species")
    .alias("mass_rank")
)
print("\n--- Rank by Body Mass (within Species) ---")
print(result.select(["species", "body_mass_g", "mass_rank"]).head(8))

# ---------------------------------------------------------
# 2. ROW_NUMBER: Sequential numbering
# ---------------------------------------------------------
result = df.sort("bill_length_mm").with_columns(
    pl.lit(1).cum_sum().over("species").alias("row_num")
)
print("\n--- Row Number (within Species, by Bill Length) ---")
print(result.select(["species", "bill_length_mm", "row_num"]).head(8))

# ---------------------------------------------------------
# 3. LAG / SHIFT: Access previous rows
# ---------------------------------------------------------
result = df.sort(["species", "body_mass_g"]).with_columns(
    pl.col("body_mass_g").shift(1).over("species").alias("prev_mass")
).with_columns(
    (pl.col("body_mass_g") - pl.col("prev_mass")).alias("mass_diff")
)
print("\n--- LAG (Previous Mass) and Difference ---")
print(result.select(["species", "body_mass_g", "prev_mass", "mass_diff"]).head(8))

# ---------------------------------------------------------
# 4. Running Aggregates
# ---------------------------------------------------------
result = df.sort(["species", "body_mass_g"]).with_columns(
    pl.col("body_mass_g").cum_sum().over("species").alias("running_mass")
)
print("\n--- Cumulative Sum of Body Mass (within Species) ---")
print(result.select(["species", "body_mass_g", "running_mass"]).head(8))
# </transform_window_polars>
