# <output_files_duckdb>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb",
# ]
# ///
import duckdb
import os

con = duckdb.connect()

# Setup dummy data in a table
con.sql("""
    CREATE TABLE summary AS 
    SELECT * FROM (VALUES 
        ('Adelie', 3701, 152), 
        ('Chinstrap', 3733, 68), 
        ('Gentoo', 5076, 124)
    ) t(species, avg_mass_g, count)
""")

# 1. Save to CSV
csv_path = "penguins_summary_db.csv"
con.sql(f"COPY summary TO '{csv_path}' (FORMAT CSV, HEADER)")
print(f"✅ Saved to CSV: {csv_path}")

# 2. Save to Parquet
parquet_path = "penguins_summary_db.parquet"
con.sql(f"COPY summary TO '{parquet_path}' (FORMAT PARQUET)")
print(f"✅ Saved to Parquet: {parquet_path}")

# 3. Save to JSON
json_path = "penguins_summary_db.json"
con.sql(f"COPY summary TO '{json_path}' (FORMAT JSON)")
print(f"✅ Saved to JSON: {json_path}")

# Clean up
for path in [csv_path, parquet_path, json_path]:
    if os.path.exists(path):
        os.remove(path)
# </output_files_duckdb>
