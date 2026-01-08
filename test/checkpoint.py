from src.writer.checkpoint import save_checkpoint, load_checkpoint

def test_checkpoint_save_and_load(tmp_path):
    cp_file = tmp_path / "checkpoint.json"

    save_checkpoint("123", 2, 45)
    data = load_checkpoint()

    assert data["last_product_id"] == "123"
    assert data["file_index"] == 2
    assert data["item_count"] == 45
