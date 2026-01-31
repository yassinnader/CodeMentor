import re

# Compile regex pattern once for efficiency
_CLEAN_PATTERN = re.compile(r'[^a-z0-9\s]')

def clean_text(text):
    """
    Lowercases and removes all non-alphanumeric and non-space characters from the input text.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    text = text.lower()
    text = _CLEAN_PATTERN.sub('', text)
    return text

def contains_keywords(text, keywords):
    """
    Checks if any of the keywords exist as whole words in the text.
    Uses set intersection for efficiency.
    """
    if not isinstance(text, str):
        raise ValueError("Text input must be a string.")
    if not keywords:
        return False
    # Use clean_text to ensure consistency
    cleaned_text = clean_text(text)
    words = set(cleaned_text.split())
    # Clean keywords and check intersection
    cleaned_keywords = {clean_text(k) for k in keywords}
    return not words.isdisjoint(cleaned_keywords)