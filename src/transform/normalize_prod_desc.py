import html
import re
import unicodedata

TAG_RE = re.compile(r"<[^>]+>")

def normalize_description(text):
    if not text:
        return ""
    # Convert HTML entities into real character
    text = html.unescape(text)
    # Remove tag element
    text = TAG_RE.sub(" ", text)
    # Standard unicode
    text = unicodedata.normalize("NFC", text)
    # Return string is replaced whitespace
    return re.sub(r"\s+", " ", text).strip()