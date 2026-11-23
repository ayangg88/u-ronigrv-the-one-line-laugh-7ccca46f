"""The One-Line Laugh — make.fun entry.

Writes a single funny line to /output/entry.txt.
"""

LINE = "I asked my phone for directions to happiness, and it's been recalculating for six years."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
