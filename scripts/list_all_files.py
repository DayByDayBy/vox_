import os
from pathlib import Path

def list_directory_contents():
    """contents of current directory and parent directory"""
    
    print("=" * 50)
    print("CURRENT WORKING DIRECTORY:")
    print(f"  {os.getcwd()}")
    print()
    
    print("CURRENT DIRECTORY CONTENTS:")
    current_dir = Path(".")
    for item in sorted(current_dir.iterdir()):
        item_type = "DIR " if item.is_dir() else "FILE"
        print(f"  {item_type}: {item.name}")
    print()
    
    print("PARENT DIRECTORY CONTENTS:")
    parent_dir = Path("..")
    for item in sorted(parent_dir.iterdir()):
        item_type = "DIR " if item.is_dir() else "FILE"
        print(f"  {item_type}: {item.name}")
    print()
    
    print("LOOKING FOR COMMON VOICE DATA:")
    possible_paths = [
        "../en/validated.tsv",
        "../validated.tsv", 
        "./en/validated.tsv",
        "./validated.tsv",
        "../en/train.tsv",
        "../train.tsv"
    ]
    
    for path in possible_paths:
        exists = Path(path).exists()
        status = "✓ FOUND" if exists else "✗ NOT FOUND"
        print(f"  {status}: {path}")
    
    print("=" * 50)

if __name__ == "__main__":
    list_directory_contents()