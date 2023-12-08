from aocd import get_data
import time


def part1(data):
    res = 0
    for line in data.split("\n"):
        digits = list(filter(lambda x: x.isdigit(), line))
        res += int(digits[0] + digits[-1])
    return res


def part2(data):
    res = 0
    for line in data.split():
        digits = []
        for i, n in enumerate(line):
            if n.isnumeric():
                digits.append(n)
            else:
                for l, num in enumerate(
                    "one two three four five six seven eight nine ten".split()
                ):
                    if line[i:].startswith(num):
                        digits.append(str(l + 1))
        res += int(digits[0] + digits[-1])
    return res


if __name__ == "__main__":
    day, year = 1, 2023
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
