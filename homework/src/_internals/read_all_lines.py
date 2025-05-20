from pathlib import Path
from typing import List


def read_all_lines(directory: str | Path) -> List[str]:
    """Lee todas las líneas de cada .txt dentro del directorio indicado."""
    directory = Path(directory)
    if not directory.is_dir():
        raise FileNotFoundError(f"Input directory '{directory}' not found")

    lines: list[str] = []
    for txt_file in directory.glob("*.txt"):
        with txt_file.open("r", encoding="utf-8") as fh:
            lines.extend(fh.readlines())
    return lines
