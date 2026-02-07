# <load_parquet_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
#     "pandas",
#     "pyarrow",
# ]
# ///
# %% [markdown]
# ### Parquet Loading with Polars
# Fast, multithreaded Parquet reading.

# %%
import polars as pl
import pathlib
import pandas as pd # For initial data gen

# Self-healing
path = pathlib.Path("data.parquet")
if not path.exists():
    pd.DataFrame({"id": range(100)}).to_parquet(path)

# %%
# Load Parquet (Eager)
df = pl.read_parquet(path)
print(f"Polars loaded {len(df)} rows.")

# Scan Parquet (Lazy - Recommended for Large Data)
query = pl.scan_parquet(path).select(["id"]).limit(5)
print("Lazy scan result:")
print(query.collect())
# </load_parquet_polars>
