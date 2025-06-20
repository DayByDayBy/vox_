from pathlib import Path

def list_root_contents():
    """contents of project root directory"""
    
    root_dir = Path(".")
    print("PROJECT ROOT CONTENTS:")
    for item in sorted(root_dir.iterdir()):
        item_type = "DIR " if item.is_dir() else "FILE"
        print(f"  {item_type}: {item.name}")
    
    print("\nLOOKING FOR TSV FILE:")
    tsv_path = Path("en/validated.tsv")
    if tsv_path.exists():
        print(f"  ✓ FOUND: {tsv_path}")
    else:
        print(f"  ✗ NOT FOUND: {tsv_path}")

if __name__ == "__main__":
    list_root_contents()