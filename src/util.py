import re


def add(a: int, b: int) -> int:
    return a + b


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def titlecase(text: str) -> str:
    return " ".join(word[:1].upper() + word[1:].lower() for word in text.split(" "))
