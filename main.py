#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes entry for make.fun.

Writes one original one-line joke about office life to /output/entry.txt.
The joke is the whole entry: a single line, under 200 characters.

The joke:
    Our open-plan office lets ideas flow freely -- mostly the idea of quitting.

Why this joke: the setup (an open-plan office where ideas flow freely) is a
plain, recognisable office image, and the punchline turns it somewhere the
reader did not see coming -- the idea flowing most freely is the idea of
quitting. The turn lands on the first read, the punchline arrives at the very
end, and the laugh comes with a wince, because everyone in an open-plan
office has had that exact thought.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

JOKE = "Our open-plan office lets ideas flow freely \u2014 mostly the idea of quitting."

MAX_JOKE_CHARS = 200


def validate_joke(joke: str) -> None:
    """Enforce the competition's entry rules: 1-200 chars, one line, UTF-8."""
    if not joke:
        raise ValueError("joke must not be empty")
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
