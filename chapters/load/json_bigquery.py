# <load_json_bigquery>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-cloud-bigquery",
# ]
# ///
# %% [markdown]
# ### JSON Loading with BigQuery
# Loading NDJSON data into BigQuery tables. Note: BigQuery requires NDJSON (Newline Delimited) for loading local files.

# %%
import unittest.mock as mock
from google.cloud import bigquery
import pathlib
import json

# Self-healing: Generate NDJSON (Native to BigQuery load)
ndjson_path = pathlib.Path("data.jsonl")
if not ndjson_path.exists():
    with open(ndjson_path, "w") as f:
        f.write('{"id": 1, "status": "active"}\n')
        f.write('{"id": 2, "status": "pending"}\n')

# %%
# Mock the client
client = mock.MagicMock(spec=bigquery.Client)

table_id = "project.dataset.json_table"
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    autodetect=True,
)

# %%
# Load NDJSON to BigQuery
with open(ndjson_path, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)
    job.result()

print(f"Mock BigQuery JSON load (NDJSON) triggered for {table_id}")
# </load_json_bigquery>
