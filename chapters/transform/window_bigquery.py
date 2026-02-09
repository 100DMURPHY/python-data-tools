# <transform_window_bigquery>
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
    
    def query(self, sql):
        print(f"\nExecuting SQL:\n{sql[:200]}...")
        
        # Return mock results based on query type
        if "RANK()" in sql:
            return MagicMock(to_dataframe=lambda: pd.DataFrame({
                'species': ['Adelie', 'Adelie', 'Adelie', 'Gentoo', 'Gentoo'],
                'body_mass_g': [4775, 4725, 4700, 6300, 6050],
                'mass_rank': [1, 2, 3, 1, 2]
            }))
        elif "ROW_NUMBER()" in sql:
            return MagicMock(to_dataframe=lambda: pd.DataFrame({
                'species': ['Adelie', 'Adelie', 'Adelie', 'Gentoo', 'Gentoo'],
                'bill_length_mm': [32.1, 33.1, 33.5, 40.9, 42.0],
                'row_num': [1, 2, 3, 1, 2]
            }))
        elif "LAG" in sql:
            return MagicMock(to_dataframe=lambda: pd.DataFrame({
                'species': ['Adelie', 'Adelie', 'Adelie', 'Gentoo', 'Gentoo'],
                'body_mass_g': [2850, 2900, 2925, 3950, 4050],
                'prev_mass': [None, 2850, 2900, None, 3950],
                'mass_diff': [None, 50, 25, None, 100]
            }))
        elif "SUM" in sql and "OVER" in sql:
            return MagicMock(to_dataframe=lambda: pd.DataFrame({
                'species': ['Adelie', 'Adelie', 'Gentoo', 'Gentoo'],
                'body_mass_g': [2850, 2900, 3950, 4050],
                'running_mass': [2850, 5750, 3950, 8000]
            }))
        else:
            return MagicMock(to_dataframe=lambda: pd.DataFrame({'status': ['OK']}))

client = MockBQClient()

# ---------------------------------------------------------
# 1. RANK: Ranking within Groups
# ---------------------------------------------------------
sql_rank = """
SELECT 
    species, body_mass_g,
    RANK() OVER (PARTITION BY species ORDER BY body_mass_g DESC) as mass_rank
FROM `my-project.dataset.penguins`
ORDER BY species, mass_rank
LIMIT 5
"""
df_rank = client.query(sql_rank).to_dataframe()
print("\n--- RANK Result ---")
print(df_rank)

# ---------------------------------------------------------
# 2. ROW_NUMBER
# ---------------------------------------------------------
sql_rownum = """
SELECT 
    species, bill_length_mm,
    ROW_NUMBER() OVER (PARTITION BY species ORDER BY bill_length_mm) as row_num
FROM `my-project.dataset.penguins`
LIMIT 5
"""
df_rownum = client.query(sql_rownum).to_dataframe()
print("\n--- ROW_NUMBER Result ---")
print(df_rownum)

# ---------------------------------------------------------
# 3. LAG
# ---------------------------------------------------------
sql_lag = """
SELECT 
    species, body_mass_g,
    LAG(body_mass_g) OVER (PARTITION BY species ORDER BY body_mass_g) as prev_mass,
    body_mass_g - LAG(body_mass_g) OVER (...) as mass_diff
FROM `my-project.dataset.penguins`
LIMIT 5
"""
df_lag = client.query(sql_lag).to_dataframe()
print("\n--- LAG Result ---")
print(df_lag)

# ---------------------------------------------------------
# 4. Running Total
# ---------------------------------------------------------
sql_running = """
SELECT 
    species, body_mass_g,
    SUM(body_mass_g) OVER (PARTITION BY species ORDER BY body_mass_g 
                           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as running_mass
FROM `my-project.dataset.penguins`
LIMIT 4
"""
df_running = client.query(sql_running).to_dataframe()
print("\n--- Running Total Result ---")
print(df_running)
# </transform_window_bigquery>
