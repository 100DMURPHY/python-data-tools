# <load_parquet_duckdb>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb",
#     "pandas",
#     "pyarrow",
# ]
# ///
# %% [markdown]
# ### Parquet Loading with DuckDB
# Direct SQL queries on Parquet files.

# %%
import duckdb
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
    # Use DuckDB itself to convert CSV to Parquet
    duckdb.sql(f"COPY (SELECT * FROM read_csv_auto('{csv_temp}')) TO '{DATA_PATH}' (FORMAT PARQUET)")

# %%
# Query Parquet directly via SQL
# DuckDB treats Parquet files as virtual tables
print("DuckDB querying penguins Parquet via SQL:")
duckdb.sql(f"SELECT species, island FROM '{DATA_PATH}' LIMIT 5").show()

# Read as relation
rel = duckdb.read_parquet(str(DATA_PATH))
print("\nRead as relation (First 5):")
rel.limit(5).show()
# </load_parquet_duckdb>
