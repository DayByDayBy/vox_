from pathlib import Path
from processing.load_and_filter import load_and_filter_tsv
from processing.save_subset import save_subset
from processing.copy_audio import copy_audio

tsv_path = "../en/validated.tsv"

source_audio_dir = Path("../en/clips/")

subset_tsv_path = Path("../voice_subset_f_20-59.tsv")
target_audio_dir = Path("../voice_subset_f_20-59/")


# not really hooked up yet, but sth like this:


def main():
    
    print("loading and filtering the tsv")
    df_filtered = load_and_filter_tsv(tsv_path)
    
    print("saving new subset tsv")
    save_subset(df_filtered, subset_tsv_path)  
    
    print("copying subset audio") 
    copy_audio_files(df_filtered, source_audio_dir, target_audio_dir)


if __name__ == "__main__":
    main()
