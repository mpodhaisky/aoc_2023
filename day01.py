from aocd import get_data
from aocd import submit
import time


def part1(data):
    return sum(
        [
            int(x[0] + x[-1])
            for line in data.split()
            for x in filter(lambda x: x.isnumeric(), line)
        ]
    )


def part2(data):
    res = 0
    for line in data.split():
        tmp = []
        for i in range(len(line)):
            if line[i].isnumeric():
                tmp.append(line[i])
            elif line[i : i + 3] == "one":
                tmp.append("1")
            elif line[i : i + 3] == "two":
                tmp.append("2")
            elif line[i : i + 5] == "three":
                tmp.append("3")
            elif line[i : i + 4] == "five":
                tmp.append("5")
            elif line[i : i + 4] == "four":
                tmp.append("4")
            elif line[i : i + 3] == "six":
                tmp.append("6")
            elif line[i : i + 5] == "seven":
                tmp.append("7")
            elif line[i : i + 5] == "eight":
                tmp.append("8")
            elif line[i : i + 4] == "nine":
                tmp.append("9")
        res += int(tmp[0] + tmp[-1])
    return res


if __name__ == "__main__":
    day, year = 1, 2023
    data = get_data(day=day, year=year)
    submit(part1(data), part="a", day=day, year=year)
    submit(part2(data), part="b", day=day, year=year)
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
