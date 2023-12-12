from aocd import get_data
import time


def part1(data):
    matrix = data.split("\n")
    up, down, left, right = -1j, 1j, -1, 1
    move = {
        "S": [up, down, left, right],
        "|": [up, down],
        "L": [right, up],
        "F": [right, down],
        "7": [left, down],
        "-": [left, right],
        "J": [left, up],
    }
    path = [
        (r, c)
        for r, row in enumerate(matrix)
        for c, col in enumerate(row)
        if col == "S"
    ]
    y, x = path[0]
    last_move = 0
    if down in move[matrix[y - 1][x]]:
        path.append((y - 1, x))
        last_move = up
    elif up in move[matrix[y + 1][x]]:
        path.append((y + 1, x))
        last_move = down
    elif left in move[matrix[y][x + 1]]:
        path.append((y, x + 1))
        last_move = right
    elif right in move[matrix[y][x - 1]]:
        path.append((y, x - 1))
        last_move = left

    while path[-1] != path[0]:
        y, x = path[-1]
        head = 1j * y + x
        last_move += sum(move[matrix[y][x]])
        path.append((int((head + last_move).imag), int((head + last_move).real)))
    path.pop()
    return len(path) // 2


def part2(data):
    pass


if __name__ == "__main__":
    day, year = 10, 2023
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
