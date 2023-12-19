from collections import defaultdict
import heapq
from aocd import get_data
import time


def part1(data):
    grid = data.split("\n")
    q = [(0, 0, 0, 0, 0, 0)]
    seen = set()
    while q:
        weight, cnt, y, x, dy, dx = heapq.heappop(q)
        if (cnt, y, x, dy, dx) in seen:
            continue
        if y == len(grid) - 1 and x == len(grid[0]) - 1 and cnt >= 4:
            return weight
        seen.add((cnt, y, x, dy, dx))

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (dy, dx) != (0, 0) and (
                ((dy, dx) == (dr, dc) and cnt == 10)
                or ((dy, dx) != (dr, dc) and cnt < 4)
                or (dy, dx) == (-dr, -dc)
                or dr + y < 0
                or dc + x < 0
                or dr + y >= len(grid)
                or dc + x >= len(grid[0])
            ):
                continue
            heapq.heappush(
                q,
                (
                    weight + int(grid[y + dr][x + dc]),
                    cnt + 1 if dr == dy and dx == dc else 1,
                    y + dr,
                    x + dc,
                    dr,
                    dc,
                ),
            )


def part2(data):
    pass


if __name__ == "__main__":
    day, year = 17, 2023
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
