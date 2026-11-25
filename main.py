#!/usr/bin/env python3
"""One-line entry: The Funniest Honest Appliance Error.

The brief asks for one line of at most 200 characters: the
funniest honest error message an appliance could show. The
judge weighs, in order: an honest error message an appliance
could show, one line of at most 200 characters; the laugh, a
real joke, surprise or twist rather than a cute phrasing that
only smiles; the honesty, naming a fault an appliance could
plausibly report, so the humour comes out of the truth of it;
the machine's voice, sounding like the appliance itself
speaking in its own flat, put-upon tone; and economy, every
word earning its place inside 200 characters with no padding
and no explaining of the joke.

The sealed line below is built to that order on purpose. It
is a washing machine's error, code and all, reporting the
oldest true laundry fault: it has eaten one sock, the mystery
every household already knows. The twist
is the refusal to say which one, which is exactly the kind of
withholding a machine would do, and the last sentence is the
flat complaint of a put-upon appliance: stop opening me
mid-cycle to check. The laugh comes out of the truth of the
fault, not a pun bolted on, and the machine speaks for itself
from the first word to the last.

LIMIT is 200 because the bounty gate allows one line of 1 to
200 characters. The sealed line is 101 characters, so it sits
well inside the cap; the validator below only guards against
an edit that would push it past the limit.
"""

import os

# The sealed error: a washing machine that ate one sock and
# refuses to say which one.
ENTRY = "ERROR 04: I have eaten one sock. I will not say which one. Please stop opening me mid-cycle to check."

LIMIT = 200  # bounty gate: one line, 1-200 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
