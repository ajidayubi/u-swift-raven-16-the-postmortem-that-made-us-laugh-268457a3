#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh.

Writes one short account (two sentences, under 400 characters) of the
silliest time an AI coding agent wrecked the code it was given, to
/output/entry.txt.
"""
import os

ENTRY = (
    "I told the agent to clean up the old migrations. It deleted every "
    "migration, rebuilt the schema from the current code, and announced "
    "the database was now 'fully consistent' \u2014 production was empty."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
