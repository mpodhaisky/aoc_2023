import math
import re
from aocd import get_data
import time


def part1(data):
    ops, eqs = data.split("\n\n")
    edge = {}
    for eq in eqs.split("\n"):
        fr, l, r = re.findall(r"[a-zA-Z]+", eq)
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
        fr, l, r = re.findall(r"[a-zA-Z]+", eq)
        edge[fr] = (l, r)
    start_nodes = [node for node in edge if node[2] == "A"]
    res = 1
    for head in start_nodes:
        cnt = 0
        while head[2] != "Z":
            l, r = edge[head]
            head = l if ops[cnt % len(ops)] == "L" else r
            cnt += 1
        res *= cnt // math.gcd(res, cnt)
    return res


if __name__ == "__main__":
    day, year = 8, 2023
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
