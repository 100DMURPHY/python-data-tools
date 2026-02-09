# <transform_pivot_duckdb>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb",
#     "pandas",
# ]
# ///
import duckdb
import pandas as pd

# ---------------------------------------------------------
# Load Dataset (Palmer Penguins)
# ---------------------------------------------------------
URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

con = duckdb.connect()
try:
    con.sql(f"CREATE TABLE penguins AS SELECT * FROM read_csv_auto('{URL}')")
    print("Loaded penguins via URL into DuckDB.")
except Exception as e:
    print(f"URL load failed: {e}. Using mock data fallback.")
    data = {
        'species': ['Adelie', 'Adelie', 'Adelie', 'Chinstrap', 'Gentoo', 'Gentoo'],
        'island': ['Torgersen', 'Torgersen', 'Dream', 'Dream', 'Biscoe', 'Biscoe'],
        'bill_length_mm': [39.1, 39.5, 40.3, 46.5, 46.1, 50.0],
        'body_mass_g': [3750, 3800, 3250, 3500, 4500, 5700]
    }
    df = pd.DataFrame(data)
    con.register('penguins', df)

# ---------------------------------------------------------
# 1. PIVOT (Long → Wide)
# ---------------------------------------------------------
# DuckDB has native PIVOT syntax
print("\n--- PIVOT: Avg Body Mass (Species x Island) ---")
pivot_result = con.sql("""
    PIVOT penguins 
    ON island 
    USING AVG(body_mass_g) 
    GROUP BY species
""").df()
print(pivot_result)

# ---------------------------------------------------------
# 2. UNPIVOT (Wide → Long)
# ---------------------------------------------------------
# First create a wide summary table
con.sql("""
    CREATE OR REPLACE TABLE wide_summary AS
    SELECT 
        species, 
        AVG(bill_length_mm) as bill_length,
        AVG(body_mass_g) as body_mass
    FROM penguins
    GROUP BY species
""")

print("\n--- Wide Summary ---")
print(con.sql("SELECT * FROM wide_summary").df())

# Unpivot it
print("\n--- UNPIVOT Result ---")
unpivot_result = con.sql("""
    SELECT species, metric, value FROM (
        SELECT species, 
               CAST(bill_length AS DOUBLE) as bill_length, 
               CAST(body_mass AS DOUBLE) as body_mass 
        FROM wide_summary
    ) UNPIVOT INCLUDE NULLS (
        value FOR metric IN (bill_length, body_mass)
    )
""").df()
print(unpivot_result)

# ---------------------------------------------------------
# 3. Crosstab with CASE WHEN (Manual Pivot)
# ---------------------------------------------------------
# More flexible approach using CASE WHEN
print("\n--- Manual Pivot with CASE WHEN ---")
manual_pivot = con.sql("""
    SELECT 
        species,
        AVG(CASE WHEN island = 'Biscoe' THEN body_mass_g END) as Biscoe,
        AVG(CASE WHEN island = 'Dream' THEN body_mass_g END) as Dream,
        AVG(CASE WHEN island = 'Torgersen' THEN body_mass_g END) as Torgersen
    FROM penguins
    GROUP BY species
""").df()
print(manual_pivot)
# </transform_pivot_duckdb>
