from aocd import get_data
import time
import sys

sys.setrecursionlimit(100000)


def part1(data):
    tiles = {(0, 0)}
    y, x = (0, 0)
    dy, dx = (0, 0)
    for line in data.split("\n"):
        move, num, _ = line.split(" ")
        num = int(num)
        if move == "L":
            dy, dx = (0, -1)
        elif move == "R":
            dy, dx = (0, 1)
        elif move == "D":
            dy, dx = (1, 0)
        elif move == "U":
            dy, dx = (-1, 0)
        for i in range(1, num + 1):
            tiles.add((y + dy * i, x + dx * i))
        y += dy * num
        x += dx * num

    min_y = min(a for a, b in tiles)
    min_x = min(b for a, b in tiles)
    max_y = max(a for a, b in tiles)
    max_x = max(b for a, b in tiles)

    def floodFill(yy, xx):
        if (yy, xx) in tiles:
            return
        tiles.add((yy, xx))
        floodFill(yy - 1, xx)
        floodFill(yy, xx + 1)
        floodFill(yy + 1, xx)
        floodFill(yy, xx - 1)

    floodFill(max_y // 2 - 50, max_x // 2)
    pic = []
    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            if (y, x) in tiles:
                line += "#"
            else:
                line += "."
        pic.append(line)
    print("\n".join(pic))
    print(len(tiles))


def part2(data):
    pass


if __name__ == "__main__":
    day, year = 18, 2023
    data = get_data(day=day, year=year)
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
