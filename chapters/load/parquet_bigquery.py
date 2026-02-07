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
import pathlib
import urllib.request

# Standard "Wrangling Hero" dataset: Palmer Penguins
CSV_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
DATA_PATH = pathlib.Path("penguins.parquet")

# Self-healing: Download and convert if missing (Local mock data)
if not DATA_PATH.exists():
    csv_temp = pathlib.Path("penguins.csv")
    if not csv_temp.exists():
        urllib.request.urlretrieve(CSV_URL, csv_temp)
    import pandas as pd # Needed for conversion
    pd.read_csv(csv_temp).to_parquet(DATA_PATH)

# %%
# Mock the client
client = mock.MagicMock(spec=bigquery.Client)

# Load configuration
table_id = "project.dataset.penguins_parquet"
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.PARQUET,
    write_disposition="WRITE_TRUNCATE",
)

# %%
# Trigger load
# Parquet is the recommended format for BigQuery due to schema persistence
with open(DATA_PATH, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)
    job.result()

print(f"Mock BigQuery Parquet load triggered for {table_id}")
# </load_parquet_bigquery>
