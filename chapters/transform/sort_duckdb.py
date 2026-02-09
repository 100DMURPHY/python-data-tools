# <transform_sort_duckdb>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb",
#     "pandas",
# ]
# ///
import duckdb
import pandas as pd
import io

# ---------------------------------------------------------
# Load Dataset (Palmer Penguins)
# ---------------------------------------------------------
URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
TABLE_NAME = "penguins"

try:
    duckdb.sql(f"CREATE OR REPLACE TABLE {TABLE_NAME} AS SELECT * FROM '{URL}'")
    print(f"Loaded data from {URL} into DuckDB table '{TABLE_NAME}'")
except Exception:
    print("Warning: Failed to load data from URL. Mocking data via Pandas.")
    data = """species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
Adelie,Torgersen,39.1,18.7,181,3750,Male
Adelie,Torgersen,39.5,17.4,186,3800,Female
Adelie,Torgersen,40.3,18.0,195,3250,Female
Adelie,Torgersen,36.7,19.3,193,3450,Female
Adelie,Torgersen,39.3,20.6,190,3650,Male
Chinstrap,Dream,46.5,17.9,192,3500,Female
Chinstrap,Dream,50.0,19.5,196,3900,Male
Gentoo,Biscoe,46.1,13.2,211,4500,Female
Gentoo,Biscoe,50.0,16.3,230,5700,Male
"""
    pandas_df = pd.read_csv(io.StringIO(data))
    duckdb.sql(f"CREATE OR REPLACE TABLE {TABLE_NAME} AS SELECT * FROM pandas_df")

# ---------------------------------------------------------
# 1. Basic Sorting (ORDER BY)
# ---------------------------------------------------------
# Sort by bill length (descending)
print("\n--- Sort: bill_length_mm DESC ---")
duckdb.sql(f"""
    SELECT species, bill_length_mm 
    FROM {TABLE_NAME} 
    ORDER BY bill_length_mm DESC 
    LIMIT 3
""").show()

# ---------------------------------------------------------
# 2. Multi-Column Sorting
# ---------------------------------------------------------
# Sort by Island (ASC), then by Body Mass (DESC)
print("\n--- Sort: Island ASC, Body Mass DESC ---")
duckdb.sql(f"""
    SELECT island, body_mass_g, species 
    FROM {TABLE_NAME} 
    ORDER BY island ASC, body_mass_g DESC 
    LIMIT 3
""").show()

# ---------------------------------------------------------
# 3. Handling Nulls (NULLS FIRST/LAST)
# ---------------------------------------------------------
# Sort by sex, putting NULLs at the end
print("\n--- Sort: Sex ASC NULLS LAST ---")
duckdb.sql(f"""
    SELECT species, sex 
    FROM {TABLE_NAME} 
    ORDER BY sex ASC NULLS LAST 
    LIMIT 3
""").show()
# </transform_sort_duckdb>
