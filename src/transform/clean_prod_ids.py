def clean_product_ids(product_ids):
    seen = set()
    cleaned = []

    for pid in product_ids:
        if not pid:
            continue

        pid = pid.strip()

        if not pid or not pid.isdigit():
            continue

        if pid in seen:
            continue

        seen.add(pid)
        cleaned.append(pid)

    return cleaned
