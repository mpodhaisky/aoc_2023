from collections import defaultdict
import heapq
from aocd import get_data
import time


def part1(data):
    grid = data.split("\n")
    grid = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""".split(
        "\n"
    )
    q = [(0, 0, 0, 0, 0, 0)]
    seen = set()
    while q:
        weight, cnt, y, x, dy, dx = heapq.heappop(q)
        if (cnt, y, x, dy, dx) in seen:
            continue
        if y == len(grid) - 1 and x == len(grid[0]) - 1:
            return weight
        seen.add((cnt, y, x, dy, dx))

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (
                (dr == dy and dx == dc and cnt == 3)
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
                    weight + int(grid[y][x]),
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
