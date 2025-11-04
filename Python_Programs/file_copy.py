import shutil
import sys
from pathlib import Path

def copy_file(source: Path, dest: Path) -> None:
    """Copy a file from source to destination."""
    try:
        shutil.copy2(source, dest)
        print(f"Successfully copied {source} -> {dest}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} source_file dest_file", file=sys.stderr)
        sys.exit(1)
    
    source = Path(sys.argv[1])
    dest = Path(sys.argv[2])
    copy_file(source, dest)

if __name__ == "__main__":
    main()