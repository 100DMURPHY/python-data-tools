# <load_csv_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
# ]
# ///
# %% [markdown]
# ### CSV Loading with Polars
# Demonstrates high-performance CSV loading.

# %%
import polars as pl
import pathlib

# Self-healing: Generate data if missing for portability
path = pathlib.Path("data.csv")
if not path.exists():
    pl.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "city": ["NY", "SF", "LA"]
    }).write_csv(path)

# %%
# Basic CSV loading (eager)
df = pl.read_csv(path)
print(f"Polars loaded {len(df)} rows:")
print(df.head())

# Lazy loading (recommended for large files)
lf = pl.scan_csv(path)
df = lf.collect()
# </load_csv_polars>
