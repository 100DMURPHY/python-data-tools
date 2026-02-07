# <load_parquet_pandas>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
#     "pyarrow",
# ]
# ///
# %% [markdown]
# ### Parquet Loading with Pandas
# Columnar data handling with PyArrow engine.

# %%
import pandas as pd
import pathlib

# Self-healing: Generate data if missing
path = pathlib.Path("data.parquet")
if not path.exists():
    pd.DataFrame({
        "id": range(100),
        "val": range(100, 200)
    }).to_parquet(path)

# %%
# Load Parquet
df = pd.read_parquet(path)
print(f"Pandas loaded Parquet with {len(df)} rows.")
print(df.head())
# </load_parquet_pandas>
