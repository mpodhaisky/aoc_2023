from collections import defaultdict, deque
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
    data = """seeds: 79 1 14 1 55 1 13 1

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".split(
        "\n"
    )
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
        for _ in range(len(q)):
            a, b = q.popleft()
            for start, end, delta in sorted(m):
                if b < start:
                    q.append((a, b))
                elif a <= start <= b:
                    if a != start:
                        q.append((a, start))
                    if b != start:
                        q.append((start + delta, min(b, end) + delta))
                elif a <= end <= b:
                    if a != end:
                        q.append((a + delta, end + delta))
                a = max(a, end)
                if a >= b:
                    continue
        print(q)
    print(min(map(lambda x: x[0], q)))


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
