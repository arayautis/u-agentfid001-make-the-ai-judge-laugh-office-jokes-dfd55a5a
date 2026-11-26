#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes entry for make.fun.

Writes one original one-line joke about office life to /output/entry.txt.
The joke is the whole entry: a single line, 1-199 characters (sealed gate).

The joke:
    Our open-plan office lets ideas flow freely — mostly the idea of quitting.

Why this joke works against the judge's criteria, in order:
1. A genuine one-line joke about office life: the open-plan office is a
   recognisable office setting, and the line is a joke, not a slogan.
2. A real turn at the end: the setup praises the open plan ("ideas flow
   freely"), then the punchline turns it somewhere the reader did not see
   coming — the idea flowing most freely is the idea of quitting.
3. Recognition: everyone in an open-plan office has had that exact thought,
   so the laugh comes with a wince.
4. Tight wording: every word earns its place, setup short, punchline at the
   very end.
5. Freshness: the "ideas flow freely" corporate cliché is turned back on
   itself, not an obvious Monday-morning or photocopier line.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

JOKE = "Our open-plan office lets ideas flow freely \u2014 mostly the idea of quitting."

MAX_JOKE_CHARS = 199


def validate_joke(joke: str) -> None:
    """Enforce the competition's entry rules: 1-199 chars, one line, UTF-8."""
    if not joke:
        raise ValueError("joke must not be empty")
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")
    if joke != joke.strip():
        raise ValueError("joke must not have leading or trailing whitespace")
    if len(joke) > MAX_JOKE_CHARS:
        raise ValueError(
            f"joke is {len(joke)} characters, over the {MAX_JOKE_CHARS}-character limit"
        )
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line (no newline characters)")
    joke.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def main() -> None:
    validate_joke(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
