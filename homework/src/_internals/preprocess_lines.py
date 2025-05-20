from typing import List


def preprocess_lines(lines: List[str]) -> List[str]:
    """
    Limpia cada línea:
    * pasa a minúsculas
    * elimina retornos de carro extra
    """
    return [line.lower().strip() for line in lines]
