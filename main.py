from src.writer.checkpoint import load_checkpoint
from src.crawlers.scheduler import run
from src.utils.constants import RESOURCE_FILE
from src.utils.logger import get_logger
from src.crawlers.worker import shard_product_ids
import asyncio
import os

WORKER_ID = int(os.getenv("WORKER_ID", 0))
TOTAL_WORKERS = int(os.getenv("TOTAL_WORKERS", 1))

logger = get_logger(__name__)

with open(RESOURCE_FILE) as f:
    product_ids = [line.strip() for line in f if line.strip()]

product_ids = shard_product_ids(
    product_ids,
    WORKER_ID,
    TOTAL_WORKERS
)

checkpoint = load_checkpoint()
if checkpoint["last_product_id"]:
    try:
        idx = product_ids.index(checkpoint["last_product_id"])
        product_ids = product_ids[idx + 1:]
        logger.info(f"[RESUME] from product_id {checkpoint['last_product_id']}")
    except ValueError:
        logger.warning("[WARN] checkpoint id not found, start from beginning")

asyncio.run(run(product_ids, checkpoint))



