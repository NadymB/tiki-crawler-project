import os
from pathlib import Path
import aiohttp
from dotenv import load_dotenv

load_dotenv()

# Crawled configure
WORKER_ID = int(os.getenv("WORKER_ID", 0))
TOTAL_WORKERS = int(os.getenv("TOTAL_WORKERS", 1))

# Runtime configure
CONCURRENT = int(os.getenv("CONCURRENT", 28))
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 1000))
RETRY= int(os.getenv("RETRY", 3))

TIMEOUT = aiohttp.ClientTimeout(
    total=int(os.getenv("TIMEOUT", 15))
)

# Data direction to save raw and cleaned data
DATA_DIR = Path(os.getenv("DATA_DIR", "data"))

# list product id path
RESOURCE_FILE = Path(
    os.getenv("RESOURCE_FILE", "resources/product_ids.csv")
)

# Notify discord
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")