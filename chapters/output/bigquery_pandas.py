# <output_bigquery_pandas>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
#     "pandas-gbq",
#     "google-cloud-bigquery",
# ]
# ///
import pandas as pd
from unittest.mock import MagicMock
import sys

# ---------------------------------------------------------
# Mocking pandas_gbq for Portability
# ---------------------------------------------------------
mock_gbq = MagicMock()
sys.modules["pandas_gbq"] = mock_gbq

def mock_to_gbq(df, destination_table, project_id, if_exists='append'):
    print(f"✅ [pandas-gbq] Uploading {len(df)} rows to {destination_table} (Project: {project_id})")
    print(f"✅ [pandas-gbq] Write Mode: {if_exists}")

mock_gbq.to_gbq = mock_to_gbq

# ---------------------------------------------------------
# BigQuery Upload via pandas-gbq
# ---------------------------------------------------------
df = pd.DataFrame({
    'species': ['Adelie', 'Chinstrap', 'Gentoo'],
    'count': [152, 68, 124]
})

table_id = "analytics.v1.penguin_counts"
project_id = "my-gcp-project"

# to_gbq is the high-level convenience method
pd.to_gbq(df, table_id, project_id=project_id, if_exists='replace')

print("\n--- BigQuery Upload Summary ---")
print(f"Target: {table_id}")
print(f"Library: pandas-gbq")
# </output_bigquery_pandas>
