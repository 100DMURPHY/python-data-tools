# <load_json_bigquery>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-cloud-bigquery",
#     "pandas",
# ]
# ///
# %% [markdown]
# ### JSON Loading with BigQuery
# Loading NDJSON data into BigQuery tables. Note: BigQuery requires NDJSON (Newline Delimited) for loading local files.

# %%
import unittest.mock as mock
from google.cloud import bigquery
import pathlib
import urllib.request
import pandas as pd # For initial conversion

# Standard "Wrangling Hero" dataset: Palmer Penguins
CSV_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
NDJSON_PATH = pathlib.Path("penguins.jsonl")

# Self-healing: Download and convert to NDJSON (Native to BigQuery load)
if not NDJSON_PATH.exists():
    csv_temp = pathlib.Path("penguins.csv")
    if not csv_temp.exists():
        urllib.request.urlretrieve(CSV_URL, csv_temp)
    pd.read_csv(csv_temp).to_json(NDJSON_PATH, orient="records", lines=True)

# %%
# Mock the client
client = mock.MagicMock(spec=bigquery.Client)

table_id = "project.dataset.penguins_json"
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    autodetect=True,
)

# %%
# Load NDJSON to BigQuery
# BigQuery requires Newline Delimited JSON (NDJSON) for direct file loads
with open(NDJSON_PATH, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)
    job.result()

print(f"Mock BigQuery JSON load (NDJSON) triggered for {table_id}")
# </load_json_bigquery>
