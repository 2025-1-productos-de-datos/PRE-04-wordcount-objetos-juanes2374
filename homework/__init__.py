"""
Paquete principal: ejecuta el flujo completo de Word Count.

Uso:
    python -m homework <ruta_entrada> <ruta_salida>
"""
from pathlib import Path
import sys

# --- dominio de negocio ---------------------------------------------------- #
def _run_pipeline(input_dir: str | Path, output_dir: str | Path) -> None:
    """Ejecuta las etapas del conteo de palabras."""
    from .src._internals.read_all_lines import read_all_lines
    from .src._internals.preprocess_lines import preprocess_lines
    from .src._internals.split_into_words import split_into_words
    from .src._internals.count_words import count_words
    from .src._internals.write_word_counts import write_word_counts

    input_dir, output_dir = Path(input_dir), Path(output_dir)
    lines      = read_all_lines(input_dir)
    clean_lines = preprocess_lines(lines)
    words      = split_into_words(clean_lines)
    counts     = count_words(words)
    write_word_counts(counts, output_dir)


# --- CLI ------------------------------------------------------------------- #
def main(argv: list[str] | None = None) -> None:
    argv = argv or sys.argv[1:]
    if len(argv) != 2:
        print("Usage: python -m homework <input_dir> <output_dir>", file=sys.stderr)
        sys.exit(1)
    _run_pipeline(argv[0], argv[1])


if __name__ == "__main__":
    main()
