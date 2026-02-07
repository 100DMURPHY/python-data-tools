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
import json

# Self-healing: Generate standard JSON
json_path = pathlib.Path("data.json")
if not json_path.exists():
    data = [
        {"id": 1, "user": "alice", "meta": {"login": "2024-01-01"}},
        {"id": 2, "user": "bob", "meta": {"login": "2024-01-02"}}
    ]
    with open(json_path, "w") as f:
        json.dump(data, f)

# Self-healing: Generate NDJSON (Newline Delimited)
ndjson_path = pathlib.Path("data.jsonl")
if not ndjson_path.exists():
    with open(ndjson_path, "w") as f:
        f.write('{"id": 1, "val": 10}\n')
        f.write('{"id": 2, "val": 20}\n')

# %%
# Load standard JSON
df_json = pd.read_json(json_path)
print("Standard JSON (Pandas):")
print(df_json.head())

# %%
# Load NDJSON (lines=True)
df_ndjson = pd.read_json(ndjson_path, lines=True)
print("\nNDJSON (lines=True):")
print(df_ndjson.head())
# </load_json_pandas>
