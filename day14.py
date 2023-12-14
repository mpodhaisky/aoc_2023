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


def cycle(grid):
    for _ in range(4):
        grid = tuple(map(lambda x: "".join(x), zip(*grid)))
        grid = [
            "#".join(
                [
                    "O" * k + "." * (len(group) - k)
                    for group in line.split("#")
                    for k in [group.count("O")]
                ]
            )
            for line in grid
        ]
        grid = tuple(map(lambda x: x[::-1], grid))
    return grid


def part2(data):
    grid = tuple(data.strip().split("\n"))
    states = []
    seen = set()
    while grid not in seen:
        states.append(grid)
        seen.add(grid)
        grid = cycle(grid)
    cycle_start = states.index(grid)
    cycle_len = len(states) - cycle_start
    grid = states[((1000000000 - cycle_start) % cycle_len) + cycle_start]
    t = 0
    for i, l in enumerate(grid[::-1], 1):
        t += l.count("O") * i
    return t


# def part2(data):
#     grid = data.strip().split("\n")
#     slow, fast = cycle(grid), cycle(cycle(grid))
#     while slow != fast:
#         slow, fast = cycle(slow), cycle(cycle(fast))
#     cycle_start = 0
#     slow = grid
#     while slow != fast:
#         slow, fast = cycle(slow), cycle(fast)
#         cycle_start += 1
#     cycle_length = 1
#     fast = cycle(slow)
#     while slow != fast:
#         fast = cycle(fast)
#         cycle_length += 1
#     for _ in range((1000000000 - cycle_start) % cycle_length + cycle_start):
#         grid = cycle(grid)
#     t = 0
#     for i, l in enumerate(grid[::-1], 1):
#         t += l.count("O") * i
#     return t


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
