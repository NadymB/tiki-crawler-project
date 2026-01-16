from src.load.file.checkpoint import load_checkpoint
from src.extract.scheduler import run
from config.paths import RESOURCE_FILE_CLEANED
from src.extract.worker import share_product_ids
from config.runtime import WORKER_ID, TOTAL_WORKERS
import logging 
import asyncio

logger = logging.getLogger(__name__)

def main():
    with open(RESOURCE_FILE_CLEANED) as f:
        product_ids = [line.strip() for line in f if line.strip()]

    # Distribute the list product IDs for each worker run
    product_ids = share_product_ids(
        product_ids,
        WORKER_ID,
        TOTAL_WORKERS
    )

    # Checkpoint to run from the last_product_id + 1 
    checkpoint = load_checkpoint()
    if checkpoint["last_product_id"]:
        try:
            idx = product_ids.index(checkpoint["last_product_id"])
            product_ids = product_ids[idx + 1:]
            logger.info(f"[RESUME] from product_id {checkpoint['last_product_id']}")
        except ValueError:
            logger.warning("[WARN] checkpoint id not found, start from beginning")

    asyncio.run(run(product_ids, checkpoint))

if __name__ == "__main__":
    main()



