# <load_cloud_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
#     "s3fs",
#     "gcsfs",
#     "fsspec",
# ]
# ///
import polars as pl
import unittest.mock as mock

# ---------------------------------------------------------
# AWS S3 (Simple Storage Service)
# ---------------------------------------------------------
# Using NYC Taxi Data (Parquet) - Public Bucket

S3_URI = "s3://nyc-tlc/trip data/yellow_tripdata_2023-01.parquet"

try:
    print(f"Attempting to scan from {S3_URI}...")
    # Polars scan_parquet is lazy and highly optimized for cloud
    # storage_options={"anon": True} for public buckets
    # Adding timeouts to fail fast
    q = pl.scan_parquet(S3_URI, storage_options={
        "anon": True,
        "client_kwargs": {"connect_timeout": 5, "read_timeout": 5}
    })
    
    # Collect first 5 rows
    df_s3 = q.limit(5).collect()
    print("Success natively reading S3!")
    print(df_s3)
except Exception as e:
    print(f"Warning: S3 Access failed ({e}). Mocking success for demo.")
    
    df_s3 = pl.DataFrame({
        "VendorID": [1, 2, 1],
        "tpep_pickup_datetime": ["2023-01-01 00:32:10", "2023-01-01 00:55:08", "2023-01-01 00:25:04"],
        "trip_distance": [0.97, 1.10, 0.20],
        "total_amount": [9.30, 14.30, 12.30]
    })
    print(df_s3)

# ---------------------------------------------------------
# Google Cloud Storage (GCS)
# ---------------------------------------------------------
# using BigQuery public data (CSV)

GCS_URI = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"

try:
    print(f"\nAttempting to read from {GCS_URI}...")
    df_gcs = pl.read_csv(GCS_URI)
    print("Success natively reading GCS!")
    print(df_gcs.head())
except Exception as e:
    print(f"Warning: GCS Access failed ({e}). Mocking success for demo.")
    
    df_gcs = pl.DataFrame({
        "name": ["Alabama", "Alaska", "Arizona"],
        "post_abbr": ["AL", "AK", "AZ"]
    })
    print(df_gcs)
# </load_cloud_polars>
