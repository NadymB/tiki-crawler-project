from src.extract.read_prod_ids import read_product_ids
from src.transform.clean_prod_ids import clean_product_ids
from src.load.write_prod_ids import write_product_ids
from config.paths import RESOURCE_FILE_CLEANED
from config.runtime import RESOURCE_FILE

def main():
    raw_ids = read_product_ids(RESOURCE_FILE)
    print(f"Extracted: {len(raw_ids)}")

    clean_ids = clean_product_ids(raw_ids)
    print(f"After clean: {len(clean_ids)}")

    write_product_ids(clean_ids, RESOURCE_FILE_CLEANED)
    print(f"Saved to {RESOURCE_FILE_CLEANED}")

if __name__ == "__main__":
    main()
