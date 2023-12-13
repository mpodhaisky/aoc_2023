from aocd import get_data
import time


def dfs(springs, nums):
    if "?" in springs:
        for i, c in enumerate(springs):
            if c == "?":
                return dfs(springs[:i] + "." + springs[i + 1 :], nums) + dfs(
                    springs[:i] + "#" + springs[i + 1 :], nums
                )
    else:
        return list(filter(lambda x: x != 0, map(len, springs.split(".")))) == nums


def part1(data):
    res = 0
    for line in data.split("\n"):
        springs, nums = line.split(" ")
        nums = list(map(int, nums.split(",")))
        res += dfs(springs, nums)
    return res


def part2(data):
    pass


if __name__ == "__main__":
    day, year = 12, 2023
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
