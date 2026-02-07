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
import pathlib
import urllib.request

# Standard "Wrangling Hero" dataset: Palmer Penguins
CSV_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
DATA_PATH = pathlib.Path("penguins.csv")

# Self-healing: Download if missing
if not DATA_PATH.exists():
    urllib.request.urlretrieve(CSV_URL, DATA_PATH)

# %%
# Mock the client for CI/verification purposes
client = mock.MagicMock(spec=bigquery.Client)

# Initialize client (Mocked for verification)
# client = bigquery.Client()

# Load CSV from local file to BigQuery table
table_id = "project.dataset.penguins"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
)

# %%
# Mocking the load_table_from_file behavior
with open(DATA_PATH, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)
    job.result()  # Wait for the job to complete

print(f"Mock BigQuery load triggered for {table_id}")
# </load_csv_bigquery>
