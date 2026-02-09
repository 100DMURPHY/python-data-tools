# <transform_sort_bigquery>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-cloud-bigquery",
#     "pandas",
#     "db-dtypes",
# ]
# ///
import unittest.mock as mock
from google.cloud import bigquery
import pandas as pd
import io

# ---------------------------------------------------------
# Mock Setup (Simulating BigQuery)
# ---------------------------------------------------------
# In a real scenario, you would use:
# client = bigquery.Client()

mock_client = mock.MagicMock(spec=bigquery.Client)
print("--- BigQuery Client Initialized (Mock) ---\n")

# Load mock data for results
data = """species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
Adelie,Torgersen,39.1,18.7,181,3750,Male
Adelie,Torgersen,39.5,17.4,186,3800,Female
Adelie,Torgersen,40.3,18.0,195,3250,Female
Adelie,Torgersen,36.7,19.3,193,3450,Female
Adelie,Torgersen,39.3,20.6,190,3650,Male
Chinstrap,Dream,46.5,17.9,192,3500,Female
Gentoo,Biscoe,46.1,13.2,211,4500,Female
"""
df_mock = pd.read_csv(io.StringIO(data))

def mock_query(query):
    print(f"Executing SQL:\n{query}\n")
    
    # We'll just sort the mock dataframe to simulate the query result
    
    result = df_mock.copy()
    
    if "ORDER BY bill_length_mm DESC" in query:
        result = result.sort_values("bill_length_mm", ascending=False)
    elif "ORDER BY island ASC, body_mass_g DESC" in query:
        result = result.sort_values(["island", "body_mass_g"], ascending=[True, False])
    elif "ORDER BY sex ASC NULLS LAST" in query:
        # Pandas handles NaNs at end by default
        result = result.sort_values("sex", ascending=True, na_position='last')
    
    # Mock row iterator
    mock_job = mock.MagicMock()
    mock_job.to_dataframe.return_value = result.head(3)
    return mock_job

mock_client.query.side_effect = mock_query

# ---------------------------------------------------------
# 1. Basic Sorting (ORDER BY)
# ---------------------------------------------------------
query = """
    SELECT species, bill_length_mm 
    FROM `my-project.dataset.penguins`
    ORDER BY bill_length_mm DESC
    LIMIT 3
"""
df = mock_client.query(query).to_dataframe()
print("--- Result ---")
print(df)

# ---------------------------------------------------------
# 2. Multi-Column Sorting
# ---------------------------------------------------------
query = """
    SELECT island, body_mass_g, species 
    FROM `my-project.dataset.penguins`
    ORDER BY island ASC, body_mass_g DESC
    LIMIT 3
"""
df = mock_client.query(query).to_dataframe()
print("\n--- Result ---")
print(df)

# ---------------------------------------------------------
# 3. Handling Nulls
# ---------------------------------------------------------
query = """
    SELECT species, sex 
    FROM `my-project.dataset.penguins`
    ORDER BY sex ASC NULLS LAST
    LIMIT 3
"""
df = mock_client.query(query).to_dataframe()
print("\n--- Result ---")
print(df)
# </transform_sort_bigquery>
