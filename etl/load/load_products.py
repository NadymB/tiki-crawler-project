from src.load.db.connect import connect
from src.load.db.config import load_config
from src.load.db.load_files import load_products_from_dir
from src.load.db.insert import insert_products
from config.paths import OUTPUT_DIR

def main():
    config = load_config()
    conn = connect(config)

    products = load_products_from_dir(OUTPUT_DIR)
    print(f"Loaded {len(products)} products")

    insert_products(conn, products) 
    print(f"Inserted {len(products)} products")

    conn.close()
    print("Done")

if __name__ == "__main__":
    main()
