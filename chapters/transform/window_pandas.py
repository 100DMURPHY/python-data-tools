# <transform_window_pandas>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
# ]
# ///
import pandas as pd
import io

# ---------------------------------------------------------
# Load Dataset (Palmer Penguins)
# ---------------------------------------------------------
URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

try:
    df = pd.read_csv(URL)
except Exception:
    data = """species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
Adelie,Torgersen,39.1,18.7,181,3750,Male
Adelie,Torgersen,39.5,17.4,186,3800,Female
Adelie,Dream,40.3,18.0,195,3250,Female
Chinstrap,Dream,46.5,17.9,192,3500,Female
Gentoo,Biscoe,46.1,13.2,211,4500,Female
Gentoo,Biscoe,50.0,16.3,230,5700,Male
"""
    df = pd.read_csv(io.StringIO(data))

# Clean up for demo
df = df.dropna(subset=['body_mass_g']).head(20)
print(f"Using {len(df)} rows for demo.")

# ---------------------------------------------------------
# 1. RANK: Ranking within Groups
# ---------------------------------------------------------
# Rank penguins by body mass within each species
df['mass_rank'] = df.groupby('species')['body_mass_g'].rank(ascending=False, method='dense')
print("\n--- Rank by Body Mass (within Species) ---")
print(df[['species', 'body_mass_g', 'mass_rank']].head(8))

# ---------------------------------------------------------
# 2. ROW_NUMBER: Sequential numbering
# ---------------------------------------------------------
# Row number within each species (ordered by bill length)
df = df.sort_values(['species', 'bill_length_mm'])
df['row_num'] = df.groupby('species').cumcount() + 1
print("\n--- Row Number (within Species, by Bill Length) ---")
print(df[['species', 'bill_length_mm', 'row_num']].head(8))

# ---------------------------------------------------------
# 3. LAG / SHIFT: Access previous rows
# ---------------------------------------------------------
# Get the previous penguin's body mass within the same species
df = df.sort_values(['species', 'body_mass_g'])
df['prev_mass'] = df.groupby('species')['body_mass_g'].shift(1)
df['mass_diff'] = df['body_mass_g'] - df['prev_mass']
print("\n--- LAG (Previous Mass) and Difference ---")
print(df[['species', 'body_mass_g', 'prev_mass', 'mass_diff']].head(8))

# ---------------------------------------------------------
# 4. CUMSUM: Running Totals
# ---------------------------------------------------------
# Cumulative count within each species
df['running_count'] = df.groupby('species').cumcount() + 1
print("\n--- Cumulative Count (within Species) ---")
print(df[['species', 'body_mass_g', 'running_count']].head(8))
# </transform_window_pandas>
