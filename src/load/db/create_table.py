import psycopg2
from src.load.db.config import load_config
from src.load.db.connect import connect

def create_table():
    commands = ("""
        CREATE TABLE products (
            id BIGINT PRIMARY KEY,
            name TEXT NOT NULL,
            url TEXT, 
            price BIGINT,
            description TEXT,
            breadcrumbs JSONB,
            images JSONB,
            created_at TIMESTAMP DEFAULT NOW() 
        )""")

    try: 
        config = load_config()
        conn = connect(config)
        with conn.cursor() as cur:
            cur.execute(commands)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 

if __name__ == '__main__':
    create_table()