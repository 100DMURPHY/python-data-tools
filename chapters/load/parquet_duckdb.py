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
import pandas as pd

# Self-healing
path = pathlib.Path("data.parquet")
if not path.exists():
    pd.DataFrame({"id": range(100)}).to_parquet(path)

# %%
# Query Parquet directly
duckdb.sql(f"SELECT COUNT(*) FROM '{path}'").show()

# Read as relation
rel = duckdb.read_parquet(str(path))
rel.limit(5).show()
# </load_parquet_duckdb>
