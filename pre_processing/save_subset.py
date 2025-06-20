def save_subset(df: pd.DataFrame, output_path: str):
    df.to_csv(output_path, sep="\t", index=False)
    
        
if __name__ == "__main__":
    
    save_subset(frame, path)