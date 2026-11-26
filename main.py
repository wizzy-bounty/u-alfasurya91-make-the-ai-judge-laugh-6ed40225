import os

LINE = "My out-of-office reply is so polite that coworkers thank it, and one now asks it for advice."


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    with open(output_path(), "wb") as fh:
        fh.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
