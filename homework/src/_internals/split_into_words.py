import re
from typing import Iterable, List


_WORD_RE = re.compile(r"[a-zA-Z']+")


def split_into_words(lines: Iterable[str]) -> List[str]:
    """Separa cada línea en palabras (solo letras y apóstrofes)."""
    words: list[str] = []
    for line in lines:
        words.extend(_WORD_RE.findall(line))
    return words
