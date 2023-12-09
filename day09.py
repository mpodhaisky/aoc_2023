from aocd import get_data
import time
from numpy import diff


def part1(data):
    res = 0
    for line in data.split("\n"):
        line = list(map(int, line.split()))
        cnt = line[-1]
        while set(line) != {0}:
            line = diff(line)
            cnt += line[-1]
        res += cnt
    return res


def part2(data):
    res = 0
    for line in data.split("\n"):
        line = list(map(int, line.split()))[::-1]
        cnt = line[-1]
        while set(line) != {0}:
            line = diff(line)
            cnt += line[-1]
        res += cnt
    return res


if __name__ == "__main__":
    day, year = 9, 2023
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
