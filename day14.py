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


# def cycle(grid):
#     for _ in range(4):
#         grid = list(map(lambda x: "".join(x), zip(*grid)))
#         grid = [
#             "#".join(
#                 ["".join(sorted(group, reverse=True)) for group in line.split("#")]
#             )
#             for line in grid
#         ]
#         grid = list(map(lambda x: x[::-1], grid))
#     return grid


def part2(data):
    grid = data.strip().split("\n")
    new_grid = []
    seen = []
    while grid not in seen:
        seen.append(grid)
        for _ in range(4):
            for line in zip(*grid):
                line = "".join(line)
                groups = line.split("#")
                new_grid.append([])
                for group in groups:
                    lo = 0
                    for i, ch in enumerate(group):
                        if ch == "o":
                            group[i], group[lo] = group[lo], group[i]
                            i += 1
                    new_grid[-1].append("".join(group))
                new_grid[-1] = "#".join(new_grid[-1])
            grid, new_grid = list(map(lambda x: x[::-1], new_grid)), []
    cycle_start = seen.index(grid)
    goal = 1000000000 - cycle_start
    seen = seen[cycle_start:]
    grid = seen[goal % len(seen)]
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
