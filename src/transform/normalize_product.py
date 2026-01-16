import json

def normalize_product(product):
    return (
        int(product["id"]),
        product["name"],
        product["url"],
        product["price"],
        product.get("description"),
        json.dumps(product.get("images_url", []), ensure_ascii=False),
        json.dumps(product.get("key", []), ensure_ascii=False)
    )