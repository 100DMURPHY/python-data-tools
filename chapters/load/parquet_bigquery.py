# <load_parquet_bigquery>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-cloud-bigquery",
#     "pandas",
#     "pyarrow",
# ]
# ///
# %% [markdown]
# ### Parquet Loading with BigQuery
# Demonstrates loading Parquet data into BigQuery tables.

# %%
import unittest.mock as mock
from google.cloud import bigquery
import pandas as pd
import pathlib

# Self-healing
path = pathlib.Path("data.parquet")
if not path.exists():
    pd.DataFrame({"id": range(100)}).to_parquet(path)

# %%
# Mock the client
client = mock.MagicMock(spec=bigquery.Client)

# Load configuration
table_id = "project.dataset.parquet_table"
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.PARQUET,
    write_disposition="WRITE_TRUNCATE",
)

# %%
# Trigger load
with open(path, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)
    job.result()

print(f"Mock BigQuery Parquet load triggered for {table_id}")
# </load_parquet_bigquery>
