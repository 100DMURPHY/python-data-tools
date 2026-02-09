# <output_files_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
# ]
# ///
import polars as pl
import os

# Create a sample summary dataframe
df = pl.DataFrame({
    'species': ['Adelie', 'Chinstrap', 'Gentoo'],
    'avg_mass_g': [3701, 3733, 5076],
    'count': [152, 68, 124]
})

# 1. Save to CSV
csv_path = "penguins_summary_pl.csv"
df.write_csv(csv_path)
print(f"✅ Saved to CSV: {csv_path}")

# 2. Save to Parquet
parquet_path = "penguins_summary_pl.parquet"
df.write_parquet(parquet_path)
print(f"✅ Saved to Parquet: {parquet_path}")

# 3. Save to JSON
json_path = "penguins_summary_pl.json"
df.write_json(json_path)
print(f"✅ Saved to JSON: {json_path}")

# Clean up
for path in [csv_path, parquet_path, json_path]:
    if os.path.exists(path):
        os.remove(path)
# </output_files_polars>
