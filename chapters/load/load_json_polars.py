# <load_json_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
# ]
# ///
# %% [markdown]
# ### JSON & NDJSON Loading with Polars
# Fast parsing for structured and semi-structured data.

# %%
import polars as pl
import pathlib
import urllib.request
import json

# Standard "Wrangling Hero" dataset: Palmer Penguins
CSV_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
JSON_PATH = pathlib.Path("penguins.json")
NDJSON_PATH = pathlib.Path("penguins.jsonl")

# Self-healing: Download and convert if missing
if not JSON_PATH.exists() or not NDJSON_PATH.exists():
    csv_temp = pathlib.Path("penguins.csv")
    if not csv_temp.exists():
        urllib.request.urlretrieve(CSV_URL, csv_temp)
    
    # Use Polars itself for high-performance conversion
    df_temp = pl.read_csv(csv_temp)
    
    # Save as standard JSON (Array of objects)
    df_temp.write_json(JSON_PATH)
    
    # Save as NDJSON (Newline Delimited)
    df_temp.write_ndjson(NDJSON_PATH)

# %%
# Load standard JSON (Eager)
# Polars parses standard JSON into memory efficiently
df_json = pl.read_json(JSON_PATH)
print("Standard JSON (Polars):")
print(df_json.head())

# %%
# Load NDJSON (Fastest)
# Newline Delimited JSON is the preferred format for high-speed Polars loading
df_ndjson = pl.read_ndjson(NDJSON_PATH)
print("\nNDJSON (Polars):")
print(df_ndjson.head())

# Scan NDJSON (Lazy - Great for large logs)
# df_lazy = pl.scan_ndjson(ndjson_path).collect()
# </load_json_polars>
