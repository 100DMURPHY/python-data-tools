# <transform_aggregate_duckdb>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb",
#     "pandas",
# ]
# ///
import duckdb
import pandas as pd # For fallback mock data

# ---------------------------------------------------------
# Load Dataset (Palmer Penguins)
# ---------------------------------------------------------
URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

# DuckDB can query the CSV URL directly!
try:
    # Create an in-memory connection
    con = duckdb.connect()
    # Check if we can reach the URL
    con.sql(f"CREATE TABLE penguins AS SELECT * FROM read_csv_auto('{URL}')")
    print(f"Loaded penguins via URL into DuckDB.")
except Exception as e:
    print(f"URL load failed: {e}. Using mock data fallback.")
    # Fallback to pandas then load into DuckDB
    data = {
        'species': ['Adelie', 'Adelie', 'Chinstrap', 'Gentoo', 'Gentoo'],
        'island': ['Torgersen', 'Torgersen', 'Dream', 'Biscoe', 'Biscoe'],
        'bill_length_mm': [39.1, 39.5, 46.5, 46.1, 50.0],
        'body_mass_g': [3750, 3800, 3500, 4500, 5700]
    }
    df = pd.DataFrame(data)
    con = duckdb.connect()
    con.register('penguins', df)

# ---------------------------------------------------------
# 1. Basic Aggregation (Mean Mass by Species)
# ---------------------------------------------------------
print("\n--- Average Body Mass by Species ---")
result1 = con.sql("""
    SELECT 
        species, 
        AVG(body_mass_g) as avg_mass 
    FROM penguins 
    GROUP BY species
""").df()
print(result1)

# ---------------------------------------------------------
# 2. Multiple Aggregations
# ---------------------------------------------------------
print("\n--- Summary Statistics by Species ---")
result2 = con.sql("""
    SELECT 
        species, 
        COUNT(*) as count,
        AVG(body_mass_g) as mean,
        MIN(body_mass_g) as min,
        MAX(body_mass_g) as max
    FROM penguins 
    GROUP BY species
""").df()
print(result2)

# ---------------------------------------------------------
# 3. Grouping by Multiple Columns
# ---------------------------------------------------------
print("\n--- Average Bill Length (Species + Island) ---")
result3 = con.sql("""
    SELECT 
        species, 
        island, 
        AVG(bill_length_mm) as avg_bill
    FROM penguins 
    GROUP BY species, island
    ORDER BY avg_bill DESC
""").df()
print(result3.head(5))

# ---------------------------------------------------------
# 4. Conditional Aggregation (SQL Filter/Case)
# ---------------------------------------------------------
# Count heavy penguins vs others per species
print("\n--- Heavy vs Normal Penguins per Species ---")
result4 = con.sql("""
    SELECT 
        species,
        COUNT(*) FILTER (WHERE body_mass_g > 4000) as heavy_count,
        COUNT(*) FILTER (WHERE body_mass_g <= 4000) as normal_count
    FROM penguins 
    GROUP BY species
""").df()
print(result4)
# </transform_aggregate_duckdb>
