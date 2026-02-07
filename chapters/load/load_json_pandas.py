# <load_json_pandas>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
# ]
# ///
# %% [markdown]
# ### JSON & NDJSON Loading with Pandas
# Handling standard JSON and Newline Delimited JSON (JSONL).

# %%
import pandas as pd
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
    df_temp = pd.read_csv(csv_temp)
    
    # Save as standard JSON (Array of objects)
    df_temp.to_json(JSON_PATH, orient="records")
    
    # Save as NDJSON (Newline Delimited)
    df_temp.to_json(NDJSON_PATH, orient="records", lines=True)

# %%
# Load standard JSON
df_json = pd.read_json(JSON_PATH)
print("Standard JSON (Pandas):")
print(df_json.head())

# %%
# Load NDJSON (lines=True)
df_ndjson = pd.read_json(NDJSON_PATH, lines=True)
print("\nNDJSON (lines=True):")
print(df_ndjson.head())
# </load_json_pandas>
