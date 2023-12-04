from aocd import get_data
from collections import Counter
import time


def part1(data):
    res = 0
    for line in data.split("\n"):
        winning, cards = line.split(": ")[1].split("|")
        cnt = 0
        for c in cards.split():
            if c in winning.split():
                cnt += 1
        res += cnt if not cnt else (1 << (cnt - 1))
    return res


def part2(data):
    total = Counter(range(len(data.split("\n"))))
    for i, line in enumerate(data.split("\n")):
        winning, cards = line.split(": ")[1].split("|")
        cnt = 0
        for c in cards.split():
            if c in winning.split():
                cnt += 1
                total[i + cnt] += total[i]
    return sum(total.values())


if __name__ == "__main__":
    day, year = 4, 2023
    data = get_data(day=day, year=year)
    t1 = time.time()
    res1 = part1(data)
    t2 = time.time()
    res2 = part2(data)
    t3 = time.time()
    print("----------------Part 1-----------------")
    print(f"time: {t2-t1}")
    print(res1)
    print("----------------Part 2-----------------")
    print(f"time: {t3-t2}")
    print(res2)
