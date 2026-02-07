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
import json

# Self-healing: Generate standard JSON
json_path = pathlib.Path("data.json")
if not json_path.exists():
    data = [{"id": i, "name": f"user_{i}"} for i in range(5)]
    with open(json_path, "w") as f:
        json.dump(data, f)

# Self-healing: Generate NDJSON
ndjson_path = pathlib.Path("data.jsonl")
if not ndjson_path.exists():
    with open(ndjson_path, "w") as f:
        for i in range(5):
            f.write(json.dumps({"id": i, "score": i * 1.5}) + "\n")

# %%
# Load standard JSON (Eager)
df_json = pl.read_json(json_path)
print("Standard JSON (Polars):")
print(df_json)

# %%
# Load NDJSON (Fastest)
df_ndjson = pl.read_ndjson(ndjson_path)
print("\nNDJSON (Polars):")
print(df_ndjson)

# Scan NDJSON (Lazy - Great for large logs)
# df_lazy = pl.scan_ndjson(ndjson_path).collect()
# </load_json_polars>
