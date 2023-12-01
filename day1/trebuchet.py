#!/usr/bin/env python3

from os import path
import re

NUMBERS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


# part 2 is a really tricky one, as you need to be careful of overlapping numbers
# eg: eightree is 83 and not just 8
def number_regex(line: str) -> str:
    pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
    return re.findall(pattern, line)


def concatenate(first: str, second: str) -> int:
    return int(str(first) + str(second))


def first_solve(lines: list[str]) -> int:
    answer = 0
    for line in lines:
        arr = []
        for i in line:
            if i.isdigit():
                arr.append(i)
        answer = answer + concatenate(arr[0], arr[0]) if len(
            arr) == 1 else answer + concatenate(arr[0], arr[-1])
    return answer


def second_solve(lines: list[str]) -> int:
    answer = 0
    for line in lines:
        arr = []
        r = number_regex(line)
        arr.append(NUMBERS[r[0]]) if r[0] in NUMBERS else arr.append(r[0])
        arr.append(NUMBERS[r[-1]]) if r[-1] in NUMBERS else arr.append(r[-1])
        answer = answer + concatenate(arr[0], arr[-1])
    return answer


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()
    print("Solution: 1 ", first_solve(lines))
    print("Solution: 2 ", second_solve(lines))
