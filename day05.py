from collections import defaultdict, deque
import math
from aocd import get_data
import time


def mapRange(seed, maps):
    res = []
    maps = sorted(maps)
    seed_start, seed_end = seed
    if seed_end < maps[0][0] or seed_start > maps[-1][1]:
        return [seed]
    for map_start, map_end, delta in maps:
        if map_start <= seed_start <= seed_end < map_end:
            res.append((seed_start + delta, seed_end + delta))
            return res
        if map_start <= seed_start <= map_end <= seed_end:
            res.append((seed_start + delta, map_end - 1 + delta))
            seed_start = map_end
    if seed_start <= seed_end:
        res.append((seed_start, seed_end))
    return res


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
    data = data.split("\n")
    seeds = list(map(int, data[0].split(":")[1].split()))

    ms = []
    for line in data[1:]:
        if line == "":
            pass
        elif len(line.split()) != 3:
            ms.append([])
        else:
            d, s, r = map(int, line.split())
            ms[-1].append((s, s + r, d - s))

    q = deque(
        [(seeds[i - 1], seeds[i] + seeds[i - 1]) for i in range(1, len(seeds), 2)]
    )
    for m in ms:
        tmp = []
        for _ in range(len(q)):
            tmp += mapRange(q.pop(), m)
        q = tmp
    return min(map(lambda x: x[0], q))


if __name__ == "__main__":
    day, year = 5, 2023
    data = get_data(day=day, year=year)
    t1 = time.time()
    part1(data)
    t2 = time.time()
    part2(data)
    t3 = time.time()
    print("----------------Part 1-----------------")
    print(f"time: {t2-t1}")
    print(part1(data))
    print("----------------Part 2-----------------")
    print(f"time: {t3-t2}")
    print(part2(data))
