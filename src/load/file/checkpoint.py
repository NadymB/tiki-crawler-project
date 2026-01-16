from config.paths import CHECKPOINT_FILE, CHECKPOINT_DIR
import json

def load_checkpoint():
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)

    if CHECKPOINT_FILE.exists():
        return json.loads(CHECKPOINT_FILE.read_text())
    return {
        "last_product_id": None,
        "file_index": 0,
        "item_count": 0
    }

def save_checkpoint(product_id, file_index, item_count):
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    
    data = {
        "last_product_id": product_id,
        "file_index": file_index,
        "item_count": item_count
    }
    tmp = CHECKPOINT_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    tmp.replace(CHECKPOINT_FILE)