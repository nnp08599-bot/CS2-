import argparse
from pathlib import Path

from db import add_demo, init_db


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import CS2 .dem file metadata into SQLite")
    parser.add_argument("demo_path", help="Path to .dem file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    demo_path = Path(args.demo_path).expanduser().resolve()

    if not demo_path.exists():
        raise SystemExit(f"File not found: {demo_path}")

    if demo_path.suffix.lower() != ".dem":
        raise SystemExit(f"Expected .dem file, got: {demo_path.name}")

    init_db()
    inserted_id = add_demo(filename=demo_path.name)
    print(f"Imported demo id={inserted_id}, filename={demo_path.name}")


if __name__ == "__main__":
    main()
