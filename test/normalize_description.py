from src.transform.normalize_prod_desc import normalize_description

def test_normalize_description_basic():
    text = "<p>Hello&nbsp;World</p>"
    assert normalize_description(text) == "Hello World"

def test_normalize_description_none():
    assert normalize_description(None) == ""

def test_normalize_description_unicode():
    text = "Cafe\u0301"
    assert normalize_description(text) == "Café"

def test_unicode_composed():
    text = "Café"
    assert normalize_description(text) == "Café"

def test_vietnamese_unicode():
    text = "Điện thoại thông minh"
    assert normalize_description(text) == "Điện thoại thông minh"

def test_emoji_preserved():
    text = "Điện thoại 📱 mới"
    assert normalize_description(text) == "Điện thoại 📱 mới"

def test_html_entity_and_unicode():
    text = "Ca&amp;fe\u0301"
    assert normalize_description(text) == "Ca&fé"

