from src.load.file.checkpoint import save_checkpoint
from config.runtime import BATCH_SIZE
from config.paths import OUTPUT_DIR
import json

async def writer(result_queue, checkpoint):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    file_index = checkpoint["file_index"]
    item_count = checkpoint["item_count"]
    f = None
    first_item = True # Check first item to add ",\n"

    def open_new_file():
        nonlocal f, first_item
        if f:
            f.write("\n]")
            f.close()

        path = OUTPUT_DIR / f"product_{file_index:04d}.json"

        # Case error while running -> continue run the last item, not run the beginning
        # If product file exsit and not empty -> write the next item, not needed add ",\n"
        if path.exists() and path.stat().st_size > 0:
            f = open(path, "r+", encoding="utf-8")
            f.seek(0, 2)  # to the end file
            # move back 1 byte to check the last character
            f.seek(f.tell() - 1)
            last_char = f.read(1)
            # if the last character is "]" -> remove it
            if last_char == "]":
                f.seek(f.tell() - 1)
                f.truncate()
            first_item = False
        else:
            # Else file empty -> write "[\n" -> write the new item
            f = open(path, "w", encoding="utf-8")
            f.write("[\n")
            first_item = True

    open_new_file()

    while True:
        product = await result_queue.get()
        if product is None:
            break

        # if has the first item -> write the next item -> else -> write ",\n"
        if first_item:
            f.write(json.dumps(product, ensure_ascii=False))
            first_item = False
        else:
            f.write(",\n" + json.dumps(product, ensure_ascii=False))
        # After write product to file -> increase item count by 1 and save checkpoint file as the last item
        item_count += 1
        save_checkpoint(product["id"], file_index, item_count)

        # check batch size enough 1000 -> forward to new file
        if item_count % BATCH_SIZE == 0:
            file_index += 1
            open_new_file()

    if f:
        f.write("\n]")
        f.close()


