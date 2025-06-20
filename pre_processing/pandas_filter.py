import pandas as pd

tsv_path = "../en/validated.tsv"


def load_and_filter_tsv(tsv_path: str) -> pd.DataFrame:
    df = pd.read_csv(tsv_path, sep="\t")
    age_group = {"twenties", "thirties", "fourties", "fifties"}
    filtered = df[(df["gender"] == "female") & (df["age"].isin(age_group))]
    return filtered


