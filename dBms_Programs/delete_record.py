"""
delete_record.py
Delete records from a CSV table by a key column (first column by default).
"""
import csv
from pathlib import Path

def delete_by_key(table_path: str, key_value: str, key_index: int = 0):
    p = Path(table_path)
    if not p.exists():
        raise FileNotFoundError(p)
    rows = []
    deleted = 0
    with p.open("r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            if row[key_index] == key_value:
                deleted += 1
                continue
            rows.append(row)
    with p.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Deleted {deleted} rows where column {key_index} == {key_value}")

if __name__ == "__main__":
    try:
        delete_by_key("dBms_Programs/employees.csv", "1")
    except FileNotFoundError as e:
        print(e)