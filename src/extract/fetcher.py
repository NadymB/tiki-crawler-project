import asyncio
from src.utils.constants import API_URL, HEADERS
from config.runtime import RETRY
from src.transform.normalize_prod_desc import normalize_description
import logging

logger = logging.getLogger(__name__)

async def fetch_product(session, product_id):
    url = API_URL.format(product_id)

    for attempt in range(1, RETRY + 1):
        try:
            async  with session.get(url, headers=HEADERS) as response:
                # Status code 429 -> ANTI BLOCK -> sleep 3s after fetch again
                if response.status == 429:
                    logger.warning("[BLOCK] product_id=%s retry=%s", product_id, attempt)
                    await asyncio.sleep(3 * attempt)
                    continue

                # Status code ! 200 -> error -> log error -> return None -> run continue the next item, not stop workflow
                if response.status != 200:
                    logger.error("[ERROR] product_id=%s status=%s", product_id, response.status)
                    return None

                data = await response.json()

                images = data.get("images")
                if not images:
                    thumbnail = data.get("thumbnail_url")
                    images = [thumbnail] if thumbnail else []

                return {
                    "id": product_id,
                    "name": data.get("name"),
                    "url": data.get("short_url"),
                    "key": data.get("breadcrumbs"),
                    "price": data.get("price"),
                    "description": normalize_description(data.get("description")),
                    "images_url": images
                }

        except Exception as e:
            logger.exception("[EXCEPTION] product_id=%s", product_id)
            return None

    logger.error("[FAIL] product_id=%s", product_id)
    return None
