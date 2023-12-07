from collections import Counter
import heapq
from aocd import get_data
import time


def part1(data):
    rank = [[] for _ in range(7)]
    card_value = dict([(b, a) for a, b in enumerate(list("23456789TJQKA"))])
    for line in data.split("\n"):
        a, b = line.split()
        value = {1: 0, 2: 1, 3: 3, 4: 5, 5: 6}
        rank[sum([value[c] for c in Counter(a).values()])].append(
            (
                list(map(lambda x: list(map(lambda y: card_value[y], list(x))), a)),
                int(b),
            )
        )
    s = [card[1] for cat in rank for card in list(sorted(cat, key=lambda x: x[0]))]
    return sum(i * n for i, n in enumerate(s, 1))


def part2(data):
    rank = [[] for _ in range(7)]
    card_value = dict([(b, a) for a, b in enumerate(list("J23456789TQKA"))])
    for line in data.split("\n"):
        a, b = line.split()
        value = {1: 0, 2: 1, 3: 3, 4: 5, 5: 6}
        j = a.count("J")
        freq = list(sorted(Counter(filter(lambda x: x != "J", a)).values()))
        if freq:
            freq[-1] += j
        else:
            freq = [j]

        rank[sum([value[c] for c in freq])].append(
            (
                list(map(lambda x: list(map(lambda y: card_value[y], list(x))), a)),
                int(b),
            )
        )
    s = [card[1] for cat in rank for card in list(sorted(cat, key=lambda x: x[0]))]
    return sum(i * n for i, n in enumerate(s, 1))


if __name__ == "__main__":
    day, year = 7, 2023
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
