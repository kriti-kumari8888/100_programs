"""
create_table.py
Simple demo: define a table schema and create a CSV file with header
"""
import csv
from pathlib import Path

def create_table(path: str, columns: list[str]):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(columns)
    print(f"Table created at {p} with columns: {columns}")

if __name__ == "__main__":
    create_table("dBms_Programs/employees.csv", ["id", "name", "age", "dept"])