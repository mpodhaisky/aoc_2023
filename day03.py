from aocd import get_data
import time
import re


def part1(data):
    matrix = data.split()
    m, n = len(matrix), len(matrix[0])
    res = 0
    for i, line in enumerate(matrix):
        for num in re.finditer(r"\d+", line):
            valid = False
            for y in range(i - 1, i + 2):
                for x in range(num.start() - 1, num.end() + 1):
                    if (
                        0 <= y < m
                        and 0 <= x < n
                        and matrix[y][x] not in "." + num.group()
                    ):
                        valid = True
            if valid:
                res += int(num.group())
    return res


def part2(data):
    matrix = data.split()
    m, n = len(matrix), len(matrix[0])
    res = 0
    gears = {}
    for i, line in enumerate(matrix):
        for num in re.finditer(r"\d+", line):
            for y in range(i - 1, i + 2):
                for x in range(num.start() - 1, num.end() + 1):
                    if 0 <= y < m and 0 <= x < n and matrix[y][x] == "*":
                        if (x, y) in gears:
                            res += int(num.group()) * gears[(x, y)]
                        else:
                            gears[(x, y)] = int(num.group())
    return res


if __name__ == "__main__":
    day, year = 3, 2023
    data = get_data(day=day, year=year)
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
