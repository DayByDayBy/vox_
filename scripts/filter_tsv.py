from pathlib import Path
from processing.load_and_filter import load_and_filter_tsv
from processing.save_subset import save_subset

def main():
    print("filtering TSV...")
    df_filtered = load_and_filter_tsv("../en/validated.tsv")
    print(f'filtered down to {len(df_filtered)} entries')
    print("saving new subset TSV")
    save_subset(df_filtered, "../voice_subset_f_20-59.tsv")
    print('done, saved')
    
    
if __name__ == "__main__":
    main()
    

    
    
    