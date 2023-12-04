from aocd import get_data
import time


def part1(data):
    pass


def part2(data):
    pass


if __name__ == "__main__":
    day, year = 1, 2018
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
