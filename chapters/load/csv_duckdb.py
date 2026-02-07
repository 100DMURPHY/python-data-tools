# <load_csv_duckdb>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb",
#     "pandas",
# ]
# ///
# %% [markdown]
# ### CSV Loading with DuckDB
# Using SQL to query CSV files directly.

# %%
import duckdb
import pathlib
import urllib.request

# Standard "Wrangling Hero" dataset: Palmer Penguins
CSV_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
DATA_PATH = pathlib.Path("penguins.csv")

# Self-healing: Download if missing
if not DATA_PATH.exists():
    urllib.request.urlretrieve(CSV_URL, DATA_PATH)

# %%
# Basic CSV loading via SQL
# DuckDB can query CSV files directly
print("DuckDB querying penguins via SQL:")
duckdb.sql(f"SELECT * FROM '{DATA_PATH}' LIMIT 5").show()
# </load_csv_duckdb>
