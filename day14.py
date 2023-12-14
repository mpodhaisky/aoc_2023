from aocd import get_data
import time


def part1(data):
    grid = data.strip().split("\n")
    new_grid = []
    t = 0
    for line in zip(*grid):
        line = "".join(line)
        groups = line.split("#")
        new_grid.append("#".join(["".join(sorted(group)[::-1]) for group in groups]))
    for i, l in enumerate(list(zip(*new_grid))[::-1], 1):
        t += l.count("O") * i
    return t


def part2(data):
    pass


if __name__ == "__main__":
    day, year = 14, 2023
    data = get_data(day=day, year=year)
    part2(data)
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
