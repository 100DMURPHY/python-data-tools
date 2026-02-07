# <load_csv_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
# ]
# ///
# %% [markdown]
# ### CSV Loading with Polars
# Demonstrates high-performance CSV loading.

# %%
import polars as pl
import pathlib
import urllib.request

# Standard "Wrangling Hero" dataset: Palmer Penguins
CSV_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
DATA_PATH = pathlib.Path("penguins.csv")

# Self-healing: Download if missing
if not DATA_PATH.exists():
    urllib.request.urlretrieve(CSV_URL, DATA_PATH)

# %%
# Basic CSV loading (eager)
# Polars is extremely fast at CSV parsing
df = pl.read_csv(DATA_PATH)
print("Polars loaded penguins dataset:")
print(df.head())

# Lazy loading (recommended for large files)
lf = pl.scan_csv(DATA_PATH)
df = lf.collect()
# </load_csv_polars>
