"""One Emoji, One Smile — entry for make.fun bounty
u-0xkianno-one-emoji-one-smile-5470751f.

Writes exactly one emoji to /output/entry.txt and nothing else.
Pure Python stdlib, deterministic, no network.

Pick: hugging face — an open-arms hug offered to a stranger: warm at
first glance, universal since 2017, clearly chosen over the default
smiley, and exactly right coming from someone unknown. (Revised from
heart hands: that pick leans a touch toward affection and is a 2021
emoji older devices may not render; see CANDIDATES.md.)
"""

import os

EMOJI = "\U0001f917"  # 🤗 hugging face

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
