from pathlib import Path
import aiohttp
import os

WORKER_ID = int(os.getenv("WORKER_ID", 0))

# Detail product URL
API_URL= "https://api.tiki.vn/product-detail/api/v1/products/{}"

#Header browser emulator -> avoid blocking from tiki
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://tiki.vn/",
}

# Runtime configure
CONCURRENT = int(os.getenv("CONCURRENT", 28))
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 1000))
RETRY= int(os.getenv("RETRY", 3))
TIMEOUT=aiohttp.ClientTimeout(total=int(os.getenv("TIMEOUT", 15)))

# list product id path
RESOURCE_FILE = Path(os.getenv("RESOURCE_FILE", "resources/product_ids.csv"))

# output data path
DATA_DIR = Path(os.getenv("DATA_DIR", "data"))
OUTPUT_DIR = DATA_DIR / "raw/tiki_products" / f"worker_{WORKER_ID}"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# checkpoint path
CHECKPOINT_DIR = DATA_DIR / "checkpoint"
CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)

CHECKPOINT_FILE = CHECKPOINT_DIR / f"worker_{WORKER_ID}.json"


