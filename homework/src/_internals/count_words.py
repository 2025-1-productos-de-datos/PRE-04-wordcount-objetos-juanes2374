from collections import Counter
from typing import Iterable, Counter as CounterType


def count_words(words: Iterable[str]) -> CounterType[str]:
    """Devuelve un Counter con las frecuencias de cada palabra."""
    return Counter(words)
