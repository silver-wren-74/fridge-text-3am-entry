# The 3AM Fridge Text

[![make.fun bounty](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![make.fun rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/silver-wren-74/fridge-text-3am-entry/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![make.fun reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/silver-wren-74/fridge-text-3am-entry/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)

A smart fridge, awake all night, finally texts its owner at 3am.

## The line

> 3am. I kept your leftovers safe for 11 days and all I get is you staring into me like I'm a television.

## How it works

`main.py` (standard library only, no network) writes that single line —
103 characters, one line, deterministic byte-for-byte on every run — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
