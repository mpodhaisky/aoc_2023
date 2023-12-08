from aocd import get_data
import time
import re


def part1(data):
    color = {"red": 12, "green": 13, "blue": 14}
    res = 0
    for i, line in enumerate(data.split("\n")):
        valid = True
        for pair in re.findall(r"\d+\s(?:green|red|blue)", line):
            cnt, col = pair.split()
            if int(cnt) > color[col]:
                valid = False
                break
        if valid:
            res += i + 1
    return res


def part2(data):
    res = 0
    for line in data.split("\n"):
        color = {"red": 0, "green": 0, "blue": 0}
        for pair in re.findall(r"\d+\s(?:green|red|blue)", line):
            cnt, col = pair.split()
            color[col] = max(int(cnt), color[col])
        res += color["red"] * color["green"] * color["blue"]
    return res


if __name__ == "__main__":
    day, year = 2, 2023
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
