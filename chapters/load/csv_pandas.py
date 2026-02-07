# <load_csv_pandas>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
# ]
# ///
# %% [markdown]
# ### CSV Loading with Pandas
# This example demonstrates how to load a CSV file, with self-healing data generation.

# %%
import pandas as pd
import pathlib

# Self-healing: Generate data if missing for portability
path = pathlib.Path("data.csv")
if not path.exists():
    pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "city": ["NY", "SF", "LA"]
    }).to_csv(path, index=False)

# %%
# Basic CSV loading
df = pd.read_csv(path)
print(f"Pandas loaded {len(df)} rows:")
print(df.head())

# With options
df = pd.read_csv(
    path,
    sep=",",
    header=0,
    dtype={"id": int, "name": str},
)
# </load_csv_pandas>
