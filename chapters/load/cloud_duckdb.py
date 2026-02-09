# <load_cloud_duckdb>
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
# AWS S3 (Simple Storage Service)
# ---------------------------------------------------------

S3_URI = "s3://nyc-tlc/trip data/yellow_tripdata_2023-01.parquet"

try:
    print(f"Attempting to query {S3_URI}...")
    # DuckDB's httpfs extension handles S3/GCS
    duckdb.sql("INSTALL httpfs; LOAD httpfs;")
    
    # Configure for anonymous access usually works for public buckets
    # duckdb.sql("SET s3_region='us-east-1';")
    
    # Query directly
    df_s3 = duckdb.sql(f"SELECT * FROM read_parquet('{S3_URI}') LIMIT 5").df()
    print("Success natively reading S3!")
    print(df_s3)
except Exception as e:
    print(f"Warning: S3 Access failed ({e}). Mocking success for demo.")
    
    # Mock output
    df_s3 = pd.DataFrame({
        "VendorID": [1, 2, 1],
        "trip_distance": [0.97, 1.10, 0.20],
        "total_amount": [9.30, 14.30, 12.30]
    })
    print(df_s3)
    
# ---------------------------------------------------------
# Google Cloud Storage (GCS)
# ---------------------------------------------------------
# DuckDB reads GCS via S3 compatibility layer or HTTPS for public files.
# For public files, HTTPS is robust.
HTTPS_URI = "https://storage.googleapis.com/cloud-samples-data/bigquery/us-states/us-states.csv"

try:
    print(f"\nAttempting to read from {HTTPS_URI}...")
    df_gcs = duckdb.sql(f"SELECT * FROM read_csv_auto('{HTTPS_URI}') LIMIT 5").df()
    print("Success natively reading GCS (via HTTPS)!")
    print(df_gcs)
except Exception as e:
    print(f"Warning: GCS Access failed ({e}). Mocking success for demo.")
    
    df_gcs = pd.DataFrame({
        "name": ["Alabama", "Alaska", "Arizona"],
        "post_abbr": ["AL", "AK", "AZ"]
    })
    print(df_gcs)

# </load_cloud_duckdb>
