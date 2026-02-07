# <load_json_duckdb>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb",
# ]
# ///
# %% [markdown]
# ### JSON Loading with DuckDB
# Direct SQL queries on JSON and NDJSON files.

# %%
import duckdb
import pathlib
import urllib.request

# Standard "Wrangling Hero" dataset: Palmer Penguins
CSV_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
JSON_PATH = pathlib.Path("penguins.json")
NDJSON_PATH = pathlib.Path("penguins.jsonl")

# Self-healing: Download and convert if missing
if not JSON_PATH.exists() or not NDJSON_PATH.exists():
    csv_temp = pathlib.Path("penguins.csv")
    if not csv_temp.exists():
        urllib.request.urlretrieve(CSV_URL, csv_temp)
    # Use DuckDB itself to convert CSV to JSON and NDJSON
    duckdb.sql(f"COPY (SELECT * FROM read_csv_auto('{csv_temp}')) TO '{JSON_PATH}' (FORMAT JSON, ARRAY TRUE)")
    duckdb.sql(f"COPY (SELECT * FROM read_csv_auto('{csv_temp}')) TO '{NDJSON_PATH}' (FORMAT JSON)")

# %%
# Query JSON directly via SQL
# DuckDB treats JSON files as virtual tables with auto-schema detection
print("Standard JSON via SQL:")
duckdb.sql(f"SELECT species, island, island FROM read_json_auto('{JSON_PATH}') LIMIT 5").show()

# Query NDJSON
print("\nNDJSON via SQL:")
duckdb.sql(f"SELECT * FROM read_json_auto('{NDJSON_PATH}') LIMIT 5").show()
# </load_json_duckdb>
