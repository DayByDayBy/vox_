import pandas as pd
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

def filter_us_english_female():
    print("Loading full TSV file...")
    
    # load full dataset (remove nrows to get all data)
    df = pd.read_csv("en/us_english_female_20-59.tsv", sep="\t")
    
    print(f"Original dataset shape: {df.shape}")
    
    # show what we're working with
    print(f"\nUnique gender values: {df['gender'].unique()}")
    print(f"Unique age values: {df['age'].unique()}")
    print(f"Unique accent values (first 10): {df['accents'].dropna().unique()[:10]}")
    
    # filter criteria
    print("\nApplying filters...")
    
    # US Eng accent (exact match)
    us_english_mask = df['accents'] == 'United States English'
    print(f"Records with 'United States English' accent: {us_english_mask.sum()}")
    
    # female/feminine
    female_mask = df['gender'] == 'female_feminine'
    print(f"Records with female_feminine gender: {female_mask.sum()}")
    
    #  age 20-59 (twenties, thirties, forties, fifties)
    # Note: from your earlier output, we saw 'twenties', 'thirties', 'fifties'
    # Let's check if 'forties' exists too
    target_ages = ['twenties', 'thirties', 'fourties', 'fifties']
    age_mask = df['age'].isin(target_ages)
    print(f"Records with target ages {target_ages}: {age_mask.sum()}")
    print(f"Age breakdown: {df[df['age'].isin(target_ages)]['age'].value_counts()}")
    
    # combine filters
    combined_mask = us_english_mask & female_mask & age_mask
    filtered_df = df[combined_mask]
    
    print(f"\nafter applying all filters:")
    print(f"final dataset shape: {filtered_df.shape}")
    
    if len(filtered_df) > 0:
        print(f"\nage distribution in filtered data:")
        print(filtered_df['age'].value_counts())
        
        print(f"\nfirst 5 rows of filtered data:")
        print(filtered_df[['client_id', 'sentence', 'age', 'gender', 'accents']].head())
        
        # new TSV file
        output_file = "en/us_english_female_20-59.tsv"
        filtered_df.to_csv(output_file, sep="\t", index=False)
        print(f"\nFiltered data saved to: {output_file}")
        print(f"Saved {len(filtered_df)} records")
        
        # some stats about the filtered set
        print(f"\nFiltered dataset statistics:")
        print(f"- Unique speakers (client_id): {filtered_df['client_id'].nunique()}")
        print(f"- Unique sentences: {filtered_df['sentence'].nunique()}")
        print(f"- Average up_votes: {filtered_df['up_votes'].mean():.2f}")
        print(f"- Average down_votes: {filtered_df['down_votes'].mean():.2f}")
        
    else:
        print("\nNo records match all the criteria!")
        print("Let's check individual filter results:")
        
        # looking for overlaps
        us_female = df[us_english_mask & female_mask]
        print(f"US English + Female: {len(us_female)} records")
        
        us_age = df[us_english_mask & age_mask]  
        print(f"US English + Target age: {len(us_age)} records")
        
        female_age = df[female_mask & age_mask]
        print(f"Female + Target age: {len(female_age)} records")

if __name__ == "__main__":
    filter_us_english_female()