from src.crawlers.fetcher import fetch_product

def shard_product_ids(product_ids, worker_id, total_workers):
    return [
        pid
        for i, pid in enumerate(product_ids)
        if i % total_workers == worker_id
    ]

async def worker(name, queue, session, result_queue):
    while True:
        product_id = await queue.get()
        if product_id is None:
            queue.task_done()
            break

        product = await fetch_product(session, product_id)
        if product:
            await result_queue.put(product)

        queue.task_done()
