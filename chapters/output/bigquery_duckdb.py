# <output_bigquery_duckdb>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb",
# ]
# ///
import duckdb

# ---------------------------------------------------------
# BigQuery Integration for DuckDB
# ---------------------------------------------------------
# DuckDB can interact with BigQuery via:
# 1. Exporting to Parquet for GCS-based loading
# 2. Using the 'bigquery' extension (experimental/community)
# 3. Reading/Writing via external object storage

con = duckdb.connect()

print("--- DuckDB Cloud Export Pattern ---")

# Setup dummy data
con.sql("CREATE TABLE summary AS SELECT 'Adelie' as species, 152 as count")

# Pattern: Export to Cloud Storage for downstream BQ ingestion
print("✅ Exporting DuckDB table to Parquet for GCS storage...")
# con.sql("COPY summary TO 'gs://my-bucket/summary.parquet' (FORMAT PARQUET)")
print("✅ Simulated: COPY summary TO 'gs://my-bucket/summary.parquet' (FORMAT PARQUET)")

print("\nNext Step: Trigger BigQuery LOAD from the Parquet file.")
# </output_bigquery_duckdb>
