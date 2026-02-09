# <output_bigquery_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
#     "google-cloud-bigquery",
#     "pyarrow",
#     "pandas",
# ]
# ///
import polars as pl
from unittest.mock import MagicMock

# ---------------------------------------------------------
# BigQuery Loading Patterns for Polars
# ---------------------------------------------------------
# Polars doesn't have a direct "write_bigquery" yet.
# Standard practice is to:
# 1. Convert to Parquet/Arrow and use BQ Load Job
# 2. Use BQ Storage Write API (via adbc or other connectors)
# 3. Convert to Pandas as a fallback

df = pl.DataFrame({
    'species': ['Adelie', 'Chinstrap', 'Gentoo'],
    'count': [152, 68, 124]
})

print("--- BigQuery Loading via Arrow (Simulated) ---")
# Pattern: Write to a buffer and send to BQ
import io
buffer = io.BytesIO()
df.write_parquet(buffer)
print(f"✅ Serialized {len(df)} rows to Parquet buffer.")

# Mocking the load from buffer
print(f"✅ BigQuery Load Job: Buffer -> table 'analytics.v1.penguin_counts'")
print("✅ Load Job Completed!")

print("\nPro Tip: For massive datasets, export Polars to Parquet in GCS first,")
print("then trigger a BigQuery 'Load' job from the GCS URI.")
# </output_bigquery_polars>
