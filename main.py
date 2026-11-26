"""Deadpan forecast for a city that does not exist.

Writes a single deadpan weather line (<=160 chars) for the invented
city of Quibbleford to /output/entry.txt.
"""

import os

FORECAST = (
    "In Quibbleford, a high of 41 degrees and light drizzle of warm "
    "custard; umbrellas advised, as the custard is both local and "
    "legally binding."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= len(FORECAST) <= 160:
        raise SystemExit("forecast must be 1-160 characters, got %d" % len(FORECAST))
    if "\n" in FORECAST or FORECAST != FORECAST.strip():
        raise SystemExit("forecast must be a single line with no padding")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORECAST)
    os.chmod(OUTPUT_PATH, 0o644)
    print("wrote %d characters to %s" % (len(FORECAST), OUTPUT_PATH))


if __name__ == "__main__":
    main()
