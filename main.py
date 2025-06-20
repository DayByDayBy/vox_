from pathlib import Path
from load_and_filter import load_and_filter_tsv
from save_subset import save_subset
from copy_audio import copy_audio_files

tsv_path = "../en/validated.tsv"

source_audio_dir = Path("../en/clips/")
target_audio_dir = Path("../voice_subset_f_20-59/")

target_audio_dir = Path("../voice_subset_f_20-59/")
subset_tsv_path = Path("../voice_subset_f_20-59.tsv")

# not really hooked up yet, but sth like this:

def main():
    
    df_filtered = load_and_filter_tsv(tsv_path)
    save_subset(df_filtered, subset_tsv_path)
    copy_audio_files(df_filtered, source_audio_dir, target_audio_dir)


if __name__ == "__main__":
    main()
