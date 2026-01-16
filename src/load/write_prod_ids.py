import csv

def write_product_ids(product_ids, output_path):
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["product_id"])

        for pid in product_ids:
            writer.writerow([pid])
