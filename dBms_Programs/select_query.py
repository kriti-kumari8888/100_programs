"""
select_query.py
Simple SELECT ... WHERE over a CSV file. Supports equality checks on one column.
"""
import csv
from pathlib import Path
from typing import Iterable


def select_where(table_path: str, where_col_index: int, where_value: str) -> Iterable[list[str]]:
    p = Path(table_path)
    if not p.exists():
        raise FileNotFoundError(p)
    with p.open("r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            if row[where_col_index] == where_value:
                yield row

if __name__ == "__main__":
    try:
        print("Rows with id == 1:")
        for r in select_where("dBms_Programs/employees.csv", 0, "1"):
            print(r)
    except FileNotFoundError as e:
        print(e)