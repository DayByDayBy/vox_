import pandas as pd
from pathlib import Path
from processing.copy_audio import copy_audio_files

def main():
    print("loading filtered TSV...")
    df = pd.read_csv("../voice_subset_f_20-59.tsv", sep="\t")
    print(f"copying {len(df)} audio files...")
    
    source_dir = Path("../en/clips/")
    target_dir = Path("../voice_subset_f_20-59/")
    
    copy_audio_files(df, source_dir, target_dir)
    print("done, audio files copied")

if __name__ == "__main__":
    main()
    
   