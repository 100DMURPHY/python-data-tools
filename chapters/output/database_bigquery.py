# <output_database_bigquery>
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
    
    def load_table_from_dataframe(self, dataframe, table_id, job_config=None):
        print(f"✅ Loading {len(dataframe)} rows into BigQuery table: {table_id}")
        mock_job = MagicMock()
        mock_job.result = lambda: print(f"✅ Load Job Completed!")
        return mock_job

client = MockBQClient()

# ---------------------------------------------------------
# BigQuery Database Load (to_sql equivalent)
# ---------------------------------------------------------
df = pd.DataFrame({
    'species': ['Adelie', 'Chinstrap', 'Gentoo'],
    'avg_mass_g': [3701, 3733, 5076]
})

table_id = "my-project.dataset.species_summary"

# Load dataframe into BigQuery
# In real usage, you'd provide a job_config to specify schema or write_disposition
job = client.load_table_from_dataframe(df, table_id)
job.result() # Wait for job to finish

print("\n--- Summary of Load (Simulated) ---")
print(f"Destination: {table_id}")
print(f"Rows Loaded: {len(df)}")
# </output_database_bigquery>
