#!/usr/bin/env python3

from os import path
import re


def first_solve(lines: list[str]) -> int:
    sum = 0
    for l in lines:
        id = int(l.split(":")[0].split("Game ")[1])
        j = re.findall(r'(\d+)\s*([a-zA-Z]+)', l)
        e = False
        for key, val in j:
            key = int(key)
            if (val == 'red' and key > 12) or (val == 'green' and key > 13) or (val == 'blue' and key > 14):
                e = True
                break
        sum += id if not e else 0

    return sum


def second_solve(lines: list[str]) -> int:
    sum = 0

    for l in lines:
        j = re.findall(r'(\d+)\s*([a-zA-Z]+)', l)
        k = {"red": 0, "green": 0, "blue": 0}
        for key, val in j:
            key = int(key)
            if (k[val] <= key):
                k[val] = key
        sum += k["red"] * k["green"] * k["blue"]

    return sum


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()
    print("Solution: 1 ", first_solve(lines))
    print("Solution: 2 ", second_solve(lines))
