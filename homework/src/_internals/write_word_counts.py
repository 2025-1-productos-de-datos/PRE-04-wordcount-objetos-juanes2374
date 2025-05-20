from pathlib import Path
from collections import Counter


def write_word_counts(counts: Counter, output_dir: str | Path) -> None:
    """Escribe el conteo en <output_dir>/wordcount.tsv (palabra \t frecuencia)."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    outfile = output_dir / "wordcount.tsv"
    with outfile.open("w", encoding="utf-8") as fh:
        for word in sorted(counts):          # orden alfabético
            fh.write(f"{word}\t{counts[word]}\n")
