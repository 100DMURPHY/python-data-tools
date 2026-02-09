# <output_files_bigquery>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-cloud-bigquery",
#     "pandas",
# ]
# ///
import pandas as pd
from unittest.mock import MagicMock

# ---------------------------------------------------------
# Mocking BigQuery Client for Portability
# ---------------------------------------------------------
class MockBQClient:
    def __init__(self):
        print("--- BigQuery Client Initialized (Mock) ---")
    
    def extract_table(self, table_ref, destination_uri, job_config=None):
        print(f"✅ Extraction Job Started: {table_ref} -> {destination_uri}")
        mock_job = MagicMock()
        mock_job.result = lambda: print(f"✅ Extraction Job Completed!")
        return mock_job

client = MockBQClient()

# ---------------------------------------------------------
# BigQuery Export (Extraction)
# ---------------------------------------------------------
# Note: To export to files from BigQuery, you typically "extract" a table 
# to a Cloud Storage bucket.

table_id = "my-project.dataset.summary"
destination_uri_csv = "gs://my-bucket/penguins.csv"
destination_uri_parquet = "gs://my-bucket/penguins.parquet"

# Export to CSV
client.extract_table(table_id, destination_uri_csv).result()

# Export to Parquet
client.extract_table(table_id, destination_uri_parquet).result()

print("\n--- Summary of Exports (Simulated) ---")
print(f"CSV: {destination_uri_csv}")
print(f"Parquet: {destination_uri_parquet}")
# </output_files_bigquery>
