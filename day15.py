from aocd import get_data
import time
from collections import defaultdict


def get_hash(eq):
    cur = 0
    for ch in eq:
        cur += ord(ch)
        cur *= 17
        cur %= 256
    return cur


def part1(data):
    data = data.split(",")
    t = 0
    for eq in data:
        t += get_hash(eq)
    return t


def part2(data):
    data = data.split(",")
    box = defaultdict(list)
    focus = defaultdict(int)
    for eq in data:
        if "-" in eq:
            lens, _ = eq.split("-")
            box[get_hash(lens)] = [l for l in box[get_hash(lens)] if l != lens]
        elif "=" in eq:
            lens, f = eq.split("=")
            if lens not in box[get_hash(lens)]:
                box[get_hash(lens)].append(lens)
            focus[lens] = int(f)
    t = 0
    for b in box:
        for i, lens in enumerate(box[b], 1):
            t += i * focus[lens] * (b + 1)
    return t


if __name__ == "__main__":
    day, year = 15, 2023
    data = get_data(day=day, year=year)
    part2(data)
    t1 = time.time()
    res1 = part1(data)
    t2 = time.time()
    res2 = part2(data)
    t3 = time.time()
    print(f"----------------day {str(day).zfill(2)}-----------------")
    print("----------------Part 1-----------------")
    print(f"time: {t2-t1}")
    print(f"flag: {res1}")
    print("----------------Part 2-----------------")
    print(f"time: {t3-t2}")
    print(f"flag: {res2}")
