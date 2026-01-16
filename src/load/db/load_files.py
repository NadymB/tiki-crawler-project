from pathlib import Path
import json

def load_products_from_dir(dir_path):
    products = []

    try:
        path = Path(dir_path)

        if not path.exists():
            raise FileNotFoundError(f"Path not found: {dir_path}")
        
        if not path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {dir_path}")

        for file in path.glob("*.json"):
            try:
                with open(file, encoding="utf-8") as f:
                    data = json.load(f)

                    if isinstance(data, list):
                        products.extend(data)
                    else: 
                        print(f"Skip {file}, not list")
            except json.JSONDecodeError:
                    print(f"Skip {file}, invalid JSON")
    except (FileNotFoundError, NotADirectoryError) as e:
        print(e)
    except (Exception) as e:
        print("Unexcepted error: ", e)

    return products