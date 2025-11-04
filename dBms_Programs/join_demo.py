"""
join_demo.py
Perform a nested-loop join between two small CSV files on a specified key column.
"""
import csv
from pathlib import Path
from typing import Iterable, List


def nested_loop_join(left_path: str, right_path: str, left_key_index: int = 0, right_key_index: int = 0) -> Iterable[List[str]]:
    p_left = Path(left_path)
    p_right = Path(right_path)
    if not p_left.exists() or not p_right.exists():
        raise FileNotFoundError("One or both input files are missing")
    with p_left.open("r", newline="") as lf, p_right.open("r", newline="") as rf:
        lreader = list(csv.reader(lf))
        rreader = list(csv.reader(rf))
        for lrow in lreader:
            for rrow in rreader:
                if lrow and rrow and lrow[left_key_index] == rrow[right_key_index]:
                    yield lrow + rrow

if __name__ == "__main__":
    # create two tiny CSVs to demo
    Path("dBms_Programs/left.csv").write_text("1,A\n2,B\n3,C\n")
    Path("dBms_Programs/right.csv").write_text("1,X\n3,Z\n4,Y\n")
    print("Join results:")
    for row in nested_loop_join("dBms_Programs/left.csv", "dBms_Programs/right.csv"):
        print(row)