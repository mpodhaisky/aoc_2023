from aocd import get_data
import time


def part1(data):
    time, distance = map(lambda x: x.split(":")[1].split(), data.split("\n"))
    res = 1
    for i in range(len(time)):
        cur = 0
        for j in range(int(time[i]) + 1):
            if j * (int(time[i]) - j) > int(distance[i]):
                cur += 1
        res *= cur
    return res


def part2(data):
    t, d = map(lambda x: int("".join(x.split(":")[1].split())), data.split("\n"))
    lo, hi = 0, t // 2
    lower_bound, upper_bound = t + 1, -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if mid * (t - mid) > d:
            lower_bound = mid
            hi = mid - 1
        else:
            lo = mid + 1
    lo, hi = t // 2, t
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if mid * (t - mid) > d:
            upper_bound = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return upper_bound - lower_bound + 1


if __name__ == "__main__":
    day, year = 6, 2023
    data = get_data(day=day, year=year)
    t1 = time.time()
    part1(data)
    t2 = time.time()
    part2(data)
    t3 = time.time()
    print("----------------Part 1-----------------")
    print(f"time: {t2-t1}")
    print(part1(data))
    print("----------------Part 2-----------------")
    print(f"time: {t3-t2}")
    print(part2(data))
