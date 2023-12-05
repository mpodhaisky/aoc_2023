from collections import defaultdict
import math
from aocd import get_data
from aocd import submit
import time


def part1(data):
    data = data.split("\n")
    seeds = list(map(int, data[0].split(":")[1].split()))

    ms = defaultdict(list)
    cur = ""
    for line in data[1:]:
        if line == "":
            pass
        elif len(line.split()) != 3:
            cur = line
        else:
            d, s, r = map(int, line.split())
            ms[cur].append((s, d, r))
    res = math.inf
    for seed in seeds:
        for m in ms:
            for r in ms[m]:
                if seed - r[0] >= 0 and r[0] + r[2] - seed >= 0:
                    seed += r[1] - r[0]
                    break
        res = min(seed, res)
    return res


def part2(data):
    pass


if __name__ == "__main__":
    day, year = 5, 2023
    data = get_data(day=day, year=year)
    t1 = time.time()

    t2 = time.time()
    res2 = part2(data)
    t3 = time.time()
    print("----------------Part 1-----------------")
    print(f"time: {t2-t1}")
    part1(data)
    print("----------------Part 2-----------------")
    print(f"time: {t3-t2}")
    part2(data)
