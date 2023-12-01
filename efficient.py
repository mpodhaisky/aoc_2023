from aocd import get_data
from aocd import submit


def solve(data):
    pass


if __name__ == "__main__":
    day, year = 1, 2023
    data = get_data(day=day, year=year)
    submit(solve(data), day=day, year=year)
