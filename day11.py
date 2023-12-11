import math
import re
from aocd import get_data
import time


def part1(data):
    matrix = list(map(list, data.split("\n")))
    galaxies = []
    row, col = [0] * len(matrix), [0] * len(matrix[0])
    cnt = 0
    for i, line in enumerate(matrix):
        if "#" not in line:
            cnt += 1000000 - 1
        row[i] = cnt
    cnt = 0
    for i, line in enumerate(zip(*matrix)):
        if "#" not in line:
            cnt += 1000000 - 1
        col[i] = cnt
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "#":
                galaxies.append((i, j))
    res = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            res += abs(
                galaxies[j][0]
                + row[galaxies[j][0]]
                - (galaxies[i][0] + row[galaxies[i][0]])
            ) + abs(
                galaxies[j][1]
                + col[galaxies[j][1]]
                - (galaxies[i][1] + col[galaxies[i][1]])
            )
    print(res)


def part2(data):
    pass


if __name__ == "__main__":
    day, year = 11, 2023
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
