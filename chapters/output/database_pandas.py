# <output_database_pandas>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
#     "sqlalchemy",
# ]
# ///
import pandas as pd
from sqlalchemy import create_all_engines, create_engine
import os

# Create a sample summary dataframe
df = pd.DataFrame({
    'species': ['Adelie', 'Chinstrap', 'Gentoo'],
    'avg_mass_g': [3701, 3733, 5076]
})

# 1. Connect to SQLite (local file)
db_path = "penguins.db"
engine = create_engine(f"sqlite:///{db_path}")

# 2. Write to Database
# - name: table name
# - con: sqlalchemy engine
# - if_exists: 'replace', 'append', or 'fail'
df.to_sql('species_summary', con=engine, if_exists='replace', index=False)
print(f"✅ Successfully wrote {len(df)} rows to 'species_summary' table in {db_path}.")

# 3. Quick verification query
with engine.connect() as conn:
    result = pd.read_sql("SELECT * FROM species_summary", conn)
    print("\n--- Rows read back from DB ---")
    print(result)

# Clean up
if os.path.exists(db_path):
    os.remove(db_path)
# </output_database_pandas>
