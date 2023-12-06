import re

def filter_text_using_regex(text):
    text = re.sub(
        r"^.{0,1}(\d\.|\s*\)\s*|\d\d\)\s*|[a-z]\)\s*|•\s*|[A-Z]\.\s+|[IVX]+\.\s*|[a-z]\.|[A-z]\.\s*|[a-z]\)\s*|\-\s*)",
        "",
        text,
    ).replace("  ", " ")
    return text.strip()