# <output_bigquery_bigquery>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-cloud-bigquery",
# ]
# ///
from google.cloud import bigquery
from unittest.mock import MagicMock

# ---------------------------------------------------------
# Mocking BigQuery Client for Portability
# ---------------------------------------------------------
class MockBQClient:
    def __init__(self):
        print("--- BigQuery Client Initialized (Mock) ---")

    def query(self, sql):
        print(f"✅ Executing BQ DDL/DML: {sql[:50]}...")
        return MagicMock()

    def load_table_from_uri(self, source_uri, table_id, job_config=None):
        print(f"✅ Loading from GCS: {source_uri} -> {table_id}")
        mock_job = MagicMock()
        mock_job.result = lambda: print("✅ BQ Load Job Completed!")
        return mock_job

client = MockBQClient()

# ---------------------------------------------------------
# BigQuery Native Loading (SQL & URI)
# ---------------------------------------------------------
# 1. Loading from Cloud Storage (Most common for large files)
source_uri = "gs://my-bucket/processed_data.parquet"
table_id = "my-project.dataset.final_summary"

job = client.load_table_from_uri(source_uri, table_id)
job.result()

# 2. BigQuery-to-BigQuery (CTAS Pattern)
sql = f"""
CREATE OR REPLACE TABLE `{table_id}_v2` AS
SELECT species, SUM(count) as total
FROM `{table_id}`
GROUP BY 1
"""
client.query(sql)

print("\n--- Summary ---")
print("✅ Demonstrated GCS-to-BQ Load and BQ SQL-based table creation.")
# </output_bigquery_bigquery>
