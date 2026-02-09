# <output_database_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
#     "adbc-driver-sqlite",
#     "sqlalchemy",
#     "pandas",
#     "pyarrow",
#     "connectorx",
# ]
# ///
import polars as pl
import os

# Create a sample summary dataframe
df = pl.DataFrame({
    'species': ['Adelie', 'Chinstrap', 'Gentoo'],
    'avg_mass_g': [3701, 3733, 5076]
})

# 1. Database Connection URI
db_path = os.path.abspath("penguins_pl.db")
uri = f"sqlite://{db_path}"

# 2. Write to Database
# - connection: DB URI or SQLAlchemy engine
# - table_name: Target table
# - if_table_exists: 'replace', 'append', or 'fail'
# Note: Polars uses ADBC or SQLAlchemy. ADBC is preferred for speed.
df.write_database(
    table_name="species_summary",
    connection=uri,
    if_table_exists="replace"
)
print(f"✅ Successfully wrote {len(df)} rows to 'species_summary' table in {db_path}.")

# 3. Quick verification (Optional)
# In a real app, you'd use pl.read_database_uri() to verify.
print("✅ Database write complete.")

# Clean up
if os.path.exists(db_path):
    os.remove(db_path)
# </output_database_polars>
