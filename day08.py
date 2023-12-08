import math
import re
from aocd import get_data
import time


def part1(data):
    ops, eqs = data.split("\n\n")
    edge = {}
    for eq in eqs.split("\n"):
        fr, l, r = re.findall(r"[A-Z]+", eq)
        edge[fr] = (l, r)
    head, cnt = "AAA", 0
    while head != "ZZZ":
        l, r = edge[head]
        head = l if ops[cnt % len(ops)] == "L" else r
        cnt += 1
    return cnt


def part2(data):
    ops, eqs = data.split("\n\n")
    edge = {}
    for eq in eqs.split("\n"):
        fr, l, r = re.findall(r"[A-Z]+", eq)
        edge[fr] = (l, r)
    start_nodes = [node for node in edge if node.endswith("A")]
    res = 1
    for head in start_nodes:
        cnt = 0
        while not head.endswith("Z"):
            l, r = edge[head]
            head = l if ops[cnt % len(ops)] == "L" else r
            cnt += 1
        res = math.lcm(res, cnt)
    return res


if __name__ == "__main__":
    day, year = 8, 2023
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
