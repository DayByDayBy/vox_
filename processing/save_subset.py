import pandas as pd
from pathlib import Path
from typing import Union

def save_subset(df: pd.DataFrame, output_path: Union[str, Path]):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)  # checking dir exists, avoid error when it doesnt
    df.to_csv(output_path, sep="\t", index=False)