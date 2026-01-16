import psycopg2
from src.transform.normalize_product import normalize_product

def insert_products(conn, products):
    sql = """ INSERT INTO products(id, name, url, price, description, images, breadcrumbs
              ) VALUES(%s, %s, %s, %s, %s, %s, %s)
              ON CONFLICT (id) DO NOTHING;"""

    rows = [normalize_product(p) for p in products[:100]]

    try:
        with conn.cursor() as cur:
            cur.executemany(sql, rows) 
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()   
        print("Insert batch failed:", error)
