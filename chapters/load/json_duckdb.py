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
import json

# Self-healing
json_path = pathlib.Path("data.json")
if not json_path.exists():
    with open(json_path, "w") as f:
        json.dump([{"id": 1, "v": "a"}, {"id": 2, "v": "b"}], f)

ndjson_path = pathlib.Path("data.jsonl")
if not ndjson_path.exists():
    with open(ndjson_path, "w") as f:
        f.write('{"id": 10, "v": "X"}\n{"id": 20, "v": "Y"}\n')

# %%
# Query JSON directly via SQL
print("Standard JSON via SQL:")
duckdb.sql(f"SELECT * FROM read_json_auto('{json_path}')").show()

# Query NDJSON
print("\nNDJSON via SQL:")
duckdb.sql(f"SELECT * FROM read_json_auto('{ndjson_path}')").show()
# </load_json_duckdb>
