"""
simple_index.py
Create an in-memory hash index for a CSV file for fast lookups by key (first column).
"""
import csv
from pathlib import Path
from typing import Dict, List


def build_index(table_path: str) -> Dict[str, List[int]]:
    index = {}
    p = Path(table_path)
    if not p.exists():
        raise FileNotFoundError(p)
    with p.open("r", newline="") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if not row:
                continue
            key = row[0]
            index.setdefault(key, []).append(i)
    return index

if __name__ == "__main__":
    try:
        idx = build_index("dBms_Programs/employees.csv")
        print("Index built for keys (sample up to 10):")
        for k in list(idx.keys())[:10]:
            print(k, "->", idx[k])
    except FileNotFoundError as e:
        print(e)