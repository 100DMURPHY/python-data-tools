# <load_parquet_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
#     "pandas",
#     "pyarrow",
# ]
# ///
# %% [markdown]
# ### Parquet Loading with Polars
# Fast, multithreaded Parquet reading.

# %%
import polars as pl
import pathlib
import urllib.request
import pandas as pd # For initial conversion

# Standard "Wrangling Hero" dataset: Palmer Penguins
CSV_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
DATA_PATH = pathlib.Path("penguins.parquet")

# Self-healing: Download and convert if missing
if not DATA_PATH.exists():
    csv_temp = pathlib.Path("penguins.csv")
    if not csv_temp.exists():
        urllib.request.urlretrieve(CSV_URL, csv_temp)
    pd.read_csv(csv_temp).to_parquet(DATA_PATH)

# %%
# Load Parquet (Eager)
# Polars is built on Apache Arrow for ultra-fast Parquet performance
df = pl.read_parquet(DATA_PATH)
print("Polars loaded penguins Parquet:")
print(df.head())

# Scan Parquet (Lazy - Recommended for Large Data)
# This allows Polars to skip reading columns/rows not needed
query = pl.scan_parquet(DATA_PATH).select(["species", "island"]).limit(5)
print("\nLazy scan result:")
print(query.collect())
# </load_parquet_polars>
