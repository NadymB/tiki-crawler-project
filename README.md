<div align="center" >
  <h1><strong>Tiki Crawler - Computer Network Basic Project</strong></h1>
</div>

## Overview 
This project is an async product crawler built with Python, asyncio and aiohttp. It is designed to: 
- Crawling detailed product information from Tiki API
- Handle request retry anti block
- Supporting resume crawling from the last product instead of restarting from the beginning.
- Using Docker multi-worker architecture to improve crawling performance by parallelizing workloads

The diagram above illustrates the full processes: 
<p align="center">
  <img src="assets/images/async_crawler_workflow.png" alt="Async Crawled Workflow Diagram">
</p>

## Input data
- Resource file: \
  A list of product IDs collected from Tiki, located in:
  ```
  resources/data
  ```
- Product Detail API:
  ```
  https://api.tiki.vn/product-detail/api/v1/products/{product_id}
  ```
## Output data 
The crawler outputs product data in JSON format, with each file containing up to 1000 products.
Each product record includes the following fields:
- `id`
- `name`
- `url`
- `key`
- `price`
- `description`
- `images_url` 
  
Output location:
  ```
  data/raw/tiki_products/worker_{WORKER_ID}
  ```
## How to run project
1. Build images
   ```
   docker build -t tiki-crawler . 
   ```
2. Run single workers:
   ```
   docker run --rm --env-file .env -v $(pwd)/data:/data tiki-crawler
   ```
## Environment variable
| Variable        | Description |
|-----------------|-------------|
| WORKER_ID       | Index of the current worker (default 0). Used for sharding product IDs. |
| TOTAL_WORKERS   | Total number of workers running in parallel. |
| CONCURRENT      | Number of concurrent async HTTP requests per worker. |
| BATCH_SIZE      | Maximum number of products per output JSON file. |
| RETRY           | Number of retry attempts for failed requests. |
| TIMEOUT         | Request timeout in seconds. |
| DATA_DIR        | Mounted data directory for output, logs, and checkpoints. |
| RESOURCE_FILE   | Input file containing product IDs. |

## Conclusion
This project demonstrates an efficient async crawler using Python and Docker for scalable data crawling.

