# <load_csv_duckdb>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb",
# ]
# ///
# %% [markdown]
# ### CSV Loading with DuckDB
# Using SQL to query CSV files directly.

# %% [markdown]
# ### CSV Loading with BigQuery
# Demonstrates loading local data to BigQuery.

# %%
import unittest.mock as mock
from google.cloud import bigquery
import pandas as pd
import pathlib

# Self-healing: Generate data if missing for portability
path = pathlib.Path("data.csv")
if not path.exists():
    import pandas as pd
    pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "city": ["NY", "SF", "LA"]
    }).to_csv(path, index=False)

# %%
# %%
# Basic CSV loading via SQL
duckdb.sql(f"SELECT * FROM '{path}'").show()
# </load_csv_duckdb>
