import pandas as pd
import shutil
from pathlib import Path
from tqdm import tqdm

def copy_audio_files(df: pd.DataFrame, source_dir: Path, target_dir: Path):
    target_dir.mkdir(parents=True, exist_ok=True)
    
    for _, row in tqdm(df.iterrows(), total=len(df), desc="copying audio files"):
        source_file = source_dir / row["path"]  # assuming "path" column exists
        target_file = target_dir / row["path"]
        
        if source_file.exists():
            shutil.copy2(source_file, target_file)
        else:
            print(f"warning: {source_file} not found")