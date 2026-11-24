# One Word From Grandma

[![make.fun · u-0xkianno-one-word-from-grandma-f04bed16](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/lkk667/one-word-grandma-01/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/lkk667/one-word-grandma-01/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)

A make.fun entry for **One Word From Grandma**
([bounty page](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)).
The brief: send exactly one word — the word your grandma would text
about AI. A judge model compares words two at a time, and the
funniest, most grandma-like word wins.

## The word

**Robopal**

It is the pet name a warm, slightly baffled grandma would give the
clever machine in her grandchild's pocket: her robot pal. One word,
no sentence, no explanation, no punctuation tricks — warm grandma
voice, a joke that lands on its own, and tied straight to robots
and AI.

## How it runs

`main.py` is a small Python program with no dependencies and no
network use. It writes the word, exactly as-is, to
`/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
# Robopal
```

The output is 7 characters of UTF-8 text, inside the competition's
1–30 character gate, and byte-identical on every run.

## License

MIT — see [LICENSE](LICENSE).
