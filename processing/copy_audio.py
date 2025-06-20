import shutil
from pathlib import Path
from tqdm import tqdm
import pandas as pd

def copy_audio_files(df: pd.DataFrame, source_dir: Path, target_dir: Path):
    target_dir.mkdir(parents=True, exist_ok=True)

    for relative_path in tqdm(df["path"], desc="copying audio files"):
        source_file = source_dir / relative_path
        target_file = target_dir / relative_path

        target_file.parent.mkdir(parents=True, exist_ok=True)  # ensure subdirs exist

        if source_file.exists():
            shutil.copy2(source_file, target_file)
        else:
            print(f"Warning: {source_file} not found")