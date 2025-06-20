import pandas as pd
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

def explore_tsv():
    print("Loading first 100 rows of TSV...")
    
    # just the first 100 rows to see structure
    df = pd.read_csv("en/validated.tsv", sep="\t", nrows=100)
    
    print(f"Shape: {df.shape}")
    print("\nColumn names:")
    for i, col in enumerate(df.columns):
        print(f"  {i}: '{col}'")
    
    print("\nFirst 5 rows:")
    print(df.head())
    
    print("\nData types:")
    print(df.dtypes)
    
    # accent-related columns or not?
    accent_cols = [col for col in df.columns if 'accent' in col.lower()]
    print(f"\nAccent-related columns: {accent_cols}")
    
    # confirm gender and age columns
    gender_cols = [col for col in df.columns if 'gender' in col.lower()]
    age_cols = [col for col in df.columns if 'age' in col.lower()]
    
    print(f"Gender columns: {gender_cols}")
    print(f"Age columns: {age_cols}")
    
    # sampling some age/gender
    if gender_cols:
        print(f"\nUnique gender values: {df[gender_cols[0]].unique()}")
    if age_cols:
        print(f"Unique age values: {df[age_cols[0]].unique()}")

if __name__ == "__main__":
    explore_tsv()