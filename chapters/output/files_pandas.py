# <output_files_pandas>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
#     "pyarrow",
# ]
# ///
import pandas as pd
import os

# Create a sample summary dataframe
data = {
    'species': ['Adelie', 'Chinstrap', 'Gentoo'],
    'avg_mass_g': [3701, 3733, 5076],
    'count': [152, 68, 124]
}
df = pd.DataFrame(data)

# 1. Save to CSV
csv_path = "penguins_summary.csv"
df.to_csv(csv_path, index=False)
print(f"✅ Saved to CSV: {csv_path}")

# 2. Save to Parquet (requires pyarrow or fastparquet)
parquet_path = "penguins_summary.parquet"
df.to_parquet(parquet_path, index=False)
print(f"✅ Saved to Parquet: {parquet_path}")

# 3. Save to JSON
json_path = "penguins_summary.json"
df.to_json(json_path, orient='records', indent=2)
print(f"✅ Saved to JSON: {json_path}")

# Clean up (silent in production, but good for demo)
for path in [csv_path, parquet_path, json_path]:
    if os.path.exists(path):
        os.remove(path)
# </output_files_pandas>
