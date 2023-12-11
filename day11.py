import math
import re
from aocd import get_data
import time


def solve(data, gap):
    matrix = list(map(list, data.split("\n")))
    m, n = len(matrix), len(matrix[0])
    galaxies = []
    row, col = [gap - 1] * m, [gap - 1] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "#":
                row[i] = col[j] = 0
                galaxies.append((i, j))
    for i in range(1, m):
        row[i] += row[i - 1]
    for i in range(1, n):
        col[i] += col[i - 1]
    res = 0
    for i, (a, b) in enumerate(galaxies):
        for c, d in galaxies[i + 1 :]:
            res += abs(row[a] + a - (row[c] + c)) + abs(col[b] + b - (col[d] + d))
    return res


if __name__ == "__main__":
    day, year = 11, 2023
    data = get_data(day=day, year=year)
    t1 = time.time()
    res1 = solve(data, 2)
    t2 = time.time()
    res2 = solve(data, 1000000)
    t3 = time.time()
    print(f"----------------day {str(day).zfill(2)}-----------------")
    print("----------------Part 1-----------------")
    print(f"time: {t2-t1}")
    print(f"flag: {res1}")
    print("----------------Part 2-----------------")
    print(f"time: {t3-t2}")
    print(f"flag: {res2}")
