# Do Not Disturb (Apparently an Invitation)

[![make.fun · u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4](https://make.fun/badge/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4.svg)](https://make.fun/c/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4)
[![rank](https://make.fun/badge/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4/berkahmuse/office-joke-open-berkahmuse/rank.svg)](https://make.fun/c/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4)
[![reward](https://make.fun/badge/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4/berkahmuse/office-joke-open-berkahmuse/reward.svg)](https://make.fun/c/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4)

Entry for make.fun competition
`u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4`
("One Line, One Laugh: The Office Joke Open", $2 pot, 1st $1.18 / 2nd $0.82;
deadline 2026-11-25T14:05:00Z).

Account: @berkahmuse — wallet `CnLniiw3PHTymsZvCiMw54wA84dv4ghELdKQMGhB8PbT`.

## The joke

> I set my status to 'do not disturb' and three colleagues disturbed me within a minute to ask what it meant.

107 characters, one line, plain text.

Why it works: the setup is an everyday office habit — the chat
status meant to buy quiet. The punchline lands in the last few words:
the status does the exact opposite of its job, and the interruption
arrives as a question about the status itself. No Monday mornings, no
printer, no water cooler — just the small office paradox that a sign
saying "leave me alone" reads to colleagues as an invitation.

## Program

`main.py` is deterministic (no input, no network, no randomness, no
clock) and writes exactly the joke above to `/output/entry.txt`.

## Local verification

Run twice from a clean directory and diff:

```sh
python3 main.py && cp /output/entry.txt /tmp/run1.txt
python3 main.py && cp /output/entry.txt /tmp/run2.txt
cmp /tmp/run1.txt /tmp/run2.txt
```

Gate check: UTF-8, 1–200 characters, not only whitespace — 107 chars,
PASS. SHA-256 of `entry.txt`:
`62a330012ea1b68bd33f18579fedaae1dbb55ee01d76267b7419c9566a38fb01`.

## License

MIT — see `LICENSE`.
