from aocd import get_data
import time


def points(m, f, part1):
    for i in range(len(m) - 1):
        if (
            part1
            and all(a == b for a, b in zip(m[: i + 1][::-1], m[i + 1 :]))
            or not part1
            and sum(
                c != d
                for a, b in zip(m[: i + 1][::-1], m[i + 1 :])
                for c, d in zip(a, b)
            )
            == 1
        ):
            return f * (i + 1)
    return 0


def solve(data, part):
    grids = data.split("\n\n")
    res = 0
    for grid in grids:
        grid = grid.split("\n")
        res += points(grid, 100, part) + points(list(zip(*grid)), 1, part)
    return res


if __name__ == "__main__":
    day, year = 13, 2023
    data = get_data(day=day, year=year)
    t1 = time.time()
    res1 = solve(data, True)
    t2 = time.time()
    res2 = solve(data, False)
    t3 = time.time()
    print(f"----------------day {str(day).zfill(2)}-----------------")
    print("----------------Part 1-----------------")
    print(f"time: {t2-t1}")
    print(f"flag: {res1}")
    print("----------------Part 2-----------------")
    print(f"time: {t3-t2}")
    print(f"flag: {res2}")
