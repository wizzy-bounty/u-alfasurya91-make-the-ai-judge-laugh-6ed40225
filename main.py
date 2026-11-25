import os

ENTRY = "Our 30-minute meeting ended on time once, so we scheduled a follow-up to investigate."


def write_entry(output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(output_dir)


if __name__ == "__main__":
    main()
