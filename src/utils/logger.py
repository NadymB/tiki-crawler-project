import logging
import os

LOG_DIR='data/logs'
os.makedirs(LOG_DIR, exist_ok=True)
WORKER_ID = os.getenv("WORKER_ID", "0")

def get_logger(name):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh = logging.FileHandler(f"{LOG_DIR}/crawled_error.log")
        fh.setFormatter(fmt)
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        logger.addHandler(fh)
        logger.addHandler(sh)
    return logger