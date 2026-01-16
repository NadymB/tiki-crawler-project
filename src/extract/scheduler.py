from config.runtime import CONCURRENT, TIMEOUT
from src.extract.worker import worker
from src.load.file.json_writer import writer
import logging
import asyncio
import aiohttp

logger = logging.getLogger(__name__)

async def run(product_ids, checkpoint):
    logger.info(f"Starting {len(product_ids)} product(s)")
    queue = asyncio.Queue()
    result_queue = asyncio.Queue()

    for pid in product_ids:
        await queue.put(pid)

    connector = aiohttp.TCPConnector(limit=CONCURRENT)
    async with aiohttp.ClientSession(timeout=TIMEOUT, connector=connector) as session:
        workers = [
            asyncio.create_task(worker(i, queue, session, result_queue))
            for i in range(CONCURRENT)
        ]

        writer_task = asyncio.create_task(writer(result_queue, checkpoint))

        await queue.join()

        for _ in workers:
            await queue.put(None)

        await asyncio.gather(*workers)

        await result_queue.put(None)
        await writer_task

    logger.info(f"Finished {len(product_ids)} product(s)")