from aocd import get_data
import time
from collections import defaultdict


def part1(data, start):
    grid = data.split("\n")

    def move(y, x, speed):
        res = []
        if (grid[y][x] == "-" and speed in [1j, -1j]) or (
            grid[y][x] == "|" and speed in [1, -1]
        ):
            res.append((y, x, 1j * speed))
            res.append((y, x, -1j * speed))
        elif (grid[y][x] == "/" and speed in [1, -1]) or (
            grid[y][x] == "\\" and speed in [1j, -1j]
        ):
            res.append((y, x, -1j * speed))
        elif (
            grid[y][x] == "/"
            and speed in [1j, -1j]
            or (grid[y][x] == "\\" and speed in [1, -1])
        ):
            res.append((y, x, 1j * speed))
        else:
            res.append((y, x, speed))
        return [
            (int((s + (1j * y + x)).imag), int((s + (1j * y + x)).real), s)
            for y, x, s in res
            if 0 <= int((s + (1j * y + x)).imag) < len(grid)
            and 0 <= int((s + (1j * y + x)).real) < len(grid[0])
        ]

    seen = {start}
    q = [start]
    while q:
        q = [pos for a, b, s in q for pos in move(a, b, s) if pos not in seen]
        for t in q:
            seen.add(t)
    return len(set([(a, b) for a, b, _ in seen]))


def part2(data):
    grid = data.split("\n")
    res = 0
    for i in range(len(grid[0])):
        res = max(res, part1(data, (len(grid) - 1, i, -1j)), part1(data, (0, i, 1j)))
    for j in range(len(grid)):
        res = max(res, part1(data, (j, 0, 1)), part1(data, (j, len(grid[0]) - 1, -1)))
    return res


if __name__ == "__main__":
    day, year = 16, 2023
    data = get_data(day=day, year=year)
    part2(data)
    t1 = time.time()
    res1 = part1(data, (0, 0, 1))
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
