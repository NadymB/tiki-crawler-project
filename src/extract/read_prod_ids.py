import csv

def read_product_ids(csv_path):
    product_ids = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if "id" not in reader.fieldnames:
            raise ValueError("CSV must contain 'id' column")

        for row in reader:
            product_ids.append(row["id"])

    return product_ids
