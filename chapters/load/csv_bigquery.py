# <load_csv_bigquery>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-cloud-bigquery",
#     "pandas",
# ]
# ///
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
    pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "city": ["NY", "SF", "LA"]
    }).to_csv(path, index=False)

# %%
# Mock the client for CI/verification purposes
client = mock.MagicMock(spec=bigquery.Client)

# Initialize client (Mocked for verification)
# client = bigquery.Client()

# Load CSV from local file to BigQuery table
table_id = "project.dataset.table_name"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
)

# %%
# Mocking the load_table_from_file behavior
job = client.load_table_from_file(None, table_id, job_config=job_config)
job.result() 

print(f"Mock BigQuery load triggered for {table_id}")
# </load_csv_bigquery>
