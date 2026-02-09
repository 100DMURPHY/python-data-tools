# <output_database_duckdb>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb",
# ]
# ///
import duckdb
import os

# 1. Connect to a persistent database file
db_path = "penguins_ddb.db"
con = duckdb.connect(db_path)

# 2. Create data and write to table
con.sql("""
    CREATE OR REPLACE TABLE species_summary AS 
    SELECT * FROM (VALUES 
        ('Adelie', 3701), 
        ('Chinstrap', 3733), 
        ('Gentoo', 5076)
    ) t(species, avg_mass_g)
""")
print(f"✅ Successfully created and wrote to 'species_summary' table in {db_path}.")

# 3. Quick verification query
result = con.sql("SELECT * FROM species_summary").df()
print("\n--- Rows read back from DB ---")
print(result)

# Close connection before cleanup
con.close()

# Clean up
if os.path.exists(db_path):
    os.remove(db_path)
# </output_database_duckdb>
