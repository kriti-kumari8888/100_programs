"""
insert_record.py
Append a record to a CSV 'table'.
"""
import csv
from pathlib import Path

def insert_record(table_path: str, record: list[str]):
    p = Path(table_path)
    if not p.exists():
        raise FileNotFoundError(f"Table file not found: {p}")
    with p.open("a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(record)
    print(f"Inserted record: {record}")

if __name__ == "__main__":
    # Example usage: append one record
    try:
        insert_record("dBms_Programs/employees.csv", ["1", "Alice", "30", "HR"])
    except FileNotFoundError as e:
        print(e)