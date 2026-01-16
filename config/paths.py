from pathlib import Path 
from config.runtime import WORKER_ID, DATA_DIR 

# list product id path after cleaning 
RESOURCE_FILE_CLEANED = Path("resources/product_ids_clean.csv") 

# output data path 
OUTPUT_DIR = DATA_DIR / "raw/tiki_products" / f"worker_{WORKER_ID}" 

# checkpoint path 
CHECKPOINT_DIR = DATA_DIR / "checkpoint" 
CHECKPOINT_FILE = CHECKPOINT_DIR / f"worker_{WORKER_ID}.json"