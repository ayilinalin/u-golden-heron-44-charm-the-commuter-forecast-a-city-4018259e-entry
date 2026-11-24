#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for a city
that does not exist to /output/entry.txt, for the make.fun bounty
u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.

The line names the invented city, gives it weather, and tries to make a
bored commuter smile on the way to work -- in the rhythm of a real
broadcast forecast, bent just enough to be funny.
"""

import os
import sys


OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


FORECAST = (
    "Mizzlewick: drizzle at 12°, winds at 25 km/h stealing umbrellas — "
    "the 7:40 bus is three minutes late, which locals call right on time."
)


def main() -> int:
    text = FORECAST.strip()
    if not text or len(text) > MAX_CHARS:
        print(f"entry invalid: {len(text)} chars", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
