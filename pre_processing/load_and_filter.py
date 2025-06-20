import pandas as pd
from pathlib import Path
from typing import Union


# self doc, really... but the basic idea is taking the TSV, grabbing the gender and
# age range needed (lol at fourties), filtering those to remove non-native
# speakers, and then to grab american voices - 20-59, us-eng, fem

def load_and_filter_tsv(tsv_path: Union[str, Path]) -> pd.DataFrame:
    
    """
    self doc, really... but the basic idea is taking the TSV, grabbing the gender 
    and age range needed (lol at fourties), filtering those to remove non-native
    speakers, and then to grab american voices - 20-59, us-eng, fem
    """

    df = pd.read_csv(tsv_path, sep="\t")

    age_group = {"twenties", "thirties", "fourties", "fifties"}
    filtered = df[
        (df["gender"] == "female") & 
        (df["age"].isin(age_group))
    ]

    # accent column normalising (some empties, etc)
    filtered["accent"] = filtered["accent"].fillna("").str.lower()

    #  non-native speaker entry filtering
    filtered = filtered[~filtered["accent"].str.contains("non native")]

    # 'american' filter 
    filtered = filtered[filtered["accent"].str.contains("american")]

    return filtered

