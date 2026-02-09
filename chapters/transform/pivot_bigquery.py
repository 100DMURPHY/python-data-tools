# <transform_pivot_bigquery>
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
        print(f"\nExecuting SQL:\n{sql}")
        
        # Return mock results based on query type
        if "PIVOT" in sql.upper():
            return MagicMock(to_dataframe=lambda: pd.DataFrame({
                'species': ['Adelie', 'Chinstrap', 'Gentoo'],
                'Biscoe': [3700.0, None, 5076.0],
                'Dream': [3688.0, 3733.0, None],
                'Torgersen': [3706.0, None, None]
            }))
        elif "UNPIVOT" in sql.upper():
            return MagicMock(to_dataframe=lambda: pd.DataFrame({
                'species': ['Adelie', 'Adelie', 'Chinstrap', 'Chinstrap', 'Gentoo', 'Gentoo'],
                'metric': ['bill_length', 'body_mass', 'bill_length', 'body_mass', 'bill_length', 'body_mass'],
                'value': [38.8, 3700.0, 48.8, 3733.0, 47.5, 5076.0]
            }))
        else:
            return MagicMock(to_dataframe=lambda: pd.DataFrame({'status': ['OK']}))

client = MockBQClient()

# ---------------------------------------------------------
# 1. BigQuery PIVOT
# ---------------------------------------------------------
sql_pivot = """
SELECT * FROM (
    SELECT species, island, body_mass_g
    FROM `my-project.dataset.penguins`
)
PIVOT (
    AVG(body_mass_g) FOR island IN ('Biscoe', 'Dream', 'Torgersen')
)
"""
df_pivot = client.query(sql_pivot).to_dataframe()
print("\n--- PIVOT Result ---")
print(df_pivot)

# ---------------------------------------------------------
# 2. BigQuery UNPIVOT
# ---------------------------------------------------------
sql_unpivot = """
SELECT * FROM (
    SELECT species, bill_length, body_mass
    FROM `my-project.dataset.penguin_summary`
)
UNPIVOT (
    value FOR metric IN (bill_length, body_mass)
)
"""
df_unpivot = client.query(sql_unpivot).to_dataframe()
print("\n--- UNPIVOT Result ---")
print(df_unpivot)
# </transform_pivot_bigquery>
