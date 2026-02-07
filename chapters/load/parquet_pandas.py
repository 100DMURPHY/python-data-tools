# <load_parquet_pandas>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
#     "pyarrow",
# ]
# ///
# %% [markdown]
# ### Parquet Loading with Pandas
# Columnar data handling with PyArrow engine.

# %%
import pandas as pd
import pathlib
import urllib.request

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
# Load Parquet
# Pandas uses the pyarrow engine by default for Parquet
df = pd.read_parquet(DATA_PATH)
print(f"Pandas loaded penguins Parquet with {len(df)} rows.")
print(df.head())
# </load_parquet_pandas>
