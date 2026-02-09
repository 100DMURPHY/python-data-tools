# <transform_window_duckdb>
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
    con.sql(f"CREATE TABLE penguins AS SELECT * FROM read_csv_auto('{URL}') LIMIT 20")
    print("Loaded 20 penguins via URL into DuckDB.")
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
# 1. RANK: Ranking within Groups
# ---------------------------------------------------------
print("\n--- RANK by Body Mass (within Species) ---")
rank_result = con.sql("""
    SELECT 
        species, body_mass_g,
        RANK() OVER (PARTITION BY species ORDER BY body_mass_g DESC) as mass_rank
    FROM penguins
    ORDER BY species, mass_rank
    LIMIT 8
""").df()
print(rank_result)

# ---------------------------------------------------------
# 2. ROW_NUMBER: Sequential numbering
# ---------------------------------------------------------
print("\n--- ROW_NUMBER (within Species, by Bill Length) ---")
rownum_result = con.sql("""
    SELECT 
        species, bill_length_mm,
        ROW_NUMBER() OVER (PARTITION BY species ORDER BY bill_length_mm) as row_num
    FROM penguins
    ORDER BY species, row_num
    LIMIT 8
""").df()
print(rownum_result)

# ---------------------------------------------------------
# 3. LAG: Access previous rows
# ---------------------------------------------------------
print("\n--- LAG (Previous Body Mass within Species) ---")
lag_result = con.sql("""
    SELECT 
        species, body_mass_g,
        LAG(body_mass_g) OVER (PARTITION BY species ORDER BY body_mass_g) as prev_mass,
        body_mass_g - LAG(body_mass_g) OVER (PARTITION BY species ORDER BY body_mass_g) as mass_diff
    FROM penguins
    ORDER BY species, body_mass_g
    LIMIT 8
""").df()
print(lag_result)

# ---------------------------------------------------------
# 4. Running Totals with SUM OVER
# ---------------------------------------------------------
print("\n--- Running Total Body Mass (within Species) ---")
running_result = con.sql("""
    SELECT 
        species, body_mass_g,
        SUM(body_mass_g) OVER (PARTITION BY species ORDER BY body_mass_g 
                               ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as running_mass
    FROM penguins
    ORDER BY species, body_mass_g
    LIMIT 8
""").df()
print(running_result)
# </transform_window_duckdb>
