# <load_csv_pandas>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
# ]
# ///
# %% [markdown]
# ### CSV Loading with Pandas
# This example demonstrates how to load a CSV file, with self-healing data generation.

# %%
import pandas as pd
import pathlib
import urllib.request

# Standard "Wrangling Hero" dataset: Palmer Penguins
CSV_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
DATA_PATH = pathlib.Path("penguins.csv")

# Self-healing: Download if missing
if not DATA_PATH.exists():
    urllib.request.urlretrieve(CSV_URL, DATA_PATH)

# %%
# Basic CSV loading
# We use the standardized penguins.csv dataset
df = pd.read_csv(DATA_PATH)
print(f"Pandas loaded {len(df)} rows:")
print(df.head())

# With options (Selective columns and handling NaNs)
df = pd.read_csv(
    DATA_PATH,
    usecols=["species", "island", "bill_length_mm"],
    na_values=["NA"],
)
print("\nSelective columns:")
print(df.head())
# </load_csv_pandas>
