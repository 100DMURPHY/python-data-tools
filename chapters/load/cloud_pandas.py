# <load_cloud_pandas>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
#     "s3fs",
#     "gcsfs",
#     "pyarrow",
# ]
# ///
import pandas as pd
import unittest.mock as mock

# ---------------------------------------------------------
# AWS S3 (Simple Storage Service)
# ---------------------------------------------------------
# Public dataset: NYC Taxi Data (Yellow Taxi, Jan 2023)
# Note: Real S3 access requires AWS credentials configured.
# We wrap this in a try/except block for demonstration resilience.

S3_URI = "s3://nyc-tlc/trip data/yellow_tripdata_2023-01.parquet"

try:
    print(f"Attempting to read from {S3_URI}...")
    # 'anon': True is required for public buckets without credentials
    # Adding timeouts to fail fast if network is down
    df_s3 = pd.read_parquet(S3_URI, storage_options={
        "anon": True,
        "client_kwargs": {"connect_timeout": 5, "read_timeout": 5}
    })
    print("Success natively reading S3!")
    print(df_s3.head())
except Exception as e:
    print(f"Warning: S3 Access failed ({e}). Mocking success for demo.")
    
    # Mock DataFrame
    df_s3 = pd.DataFrame({
        "VendorID": [1, 2, 1],
        "tpep_pickup_datetime": ["2023-01-01 00:32:10", "2023-01-01 00:55:08", "2023-01-01 00:25:04"],
        "passenger_count": [1.0, 1.0, 2.0],
        "trip_distance": [0.97, 1.10, 0.20],
        "total_amount": [9.30, 14.30, 12.30]
    })
    print(df_s3.head())


# ---------------------------------------------------------
# Google Cloud Storage (GCS)
# ---------------------------------------------------------
# Public dataset: BigQuery Public Data (US States)

GCS_URI = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"

try:
    print(f"\nAttempting to read from {GCS_URI}...")
    df_gcs = pd.read_csv(GCS_URI)
    print("Success natively reading GCS!")
    print(df_gcs.head())
except Exception as e:
    print(f"Warning: GCS Access failed ({e}). Mocking success for demo.")
    
    df_gcs = pd.DataFrame({
        "name": ["Alabama", "Alaska", "Arizona"],
        "post_abbr": ["AL", "AK", "AZ"]
    })
    print(df_gcs.head())

# </load_cloud_pandas>
