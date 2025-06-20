
import pandas as pd
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

def analyze_accents():
    print("Loading TSV to analyze accents...")
    
    
    df = pd.read_csv("en/validated.tsv", sep="\t", nrows=10000)
    
    print(f"Loaded {len(df)} rows")
    
    # basic accent info
    accent_col = df['accents']
    
    print(f"\nTotal entries: {len(accent_col)}")
    print(f"Non-null accent entries: {accent_col.notna().sum()}")
    print(f"Null/missing accent entries: {accent_col.isna().sum()}")
    print(f"Percentage with accent data: {(accent_col.notna().sum() / len(accent_col)) * 100:.1f}%")
    
    # unique accents (excluding NaN)
    unique_accents = accent_col.dropna().unique()
    print(f"\nnumber of unique accents: {len(unique_accents)}")
    
    print("\nunique accent values:")
    for accent in sorted(unique_accents):
        print(f"  '{accent}'")
    
    # count frequency of each accent
    print("\naccent frequency counts:")
    accent_counts = accent_col.value_counts(dropna=False)
    print(accent_counts)
    
    # check if accents column contains multiple accents per entry
    non_null_accents = accent_col.dropna()
    if len(non_null_accents) > 0:
        print(f"\nExample accent entries (first 10):")
        for i, accent in enumerate(non_null_accents.head(10)):
            print(f"  {i+1}: '{accent}'")
        
        # look for multi-accent entries (comma-separated, etc.)
        multi_accent_entries = non_null_accents[non_null_accents.str.contains(',|;|\|', na=False)]
        if len(multi_accent_entries) > 0:
            print(f"\nFound {len(multi_accent_entries)} entries with multiple accents:")
            for accent in multi_accent_entries.head(5):
                print(f"  '{accent}'")

if __name__ == "__main__":
    analyze_accents()