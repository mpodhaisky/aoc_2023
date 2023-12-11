from aocd import get_data
import time


def part1(data):
    move = {
        "|": [[1, 0], [-1, 0]],
        "L": [[-1, 0], [0, 1]],
        "F": [[1, 0], [0, 1]],
        "7": [[1, 0], [0, -1]],
        "-": [[0, 1], [0, -1]],
        "J": [[-1, 0], [0, -1]],
        ".": [[0, 0]],
    }
    matrix = list(map(list, data.split("\n")))
    m, n = len(matrix), len(matrix[0])
    last_move = [-1, -1]
    h_i, h_j = -1, -1
    cnt = 1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "S":
                if matrix[i - 1][j] in "|7F":
                    h_i, h_j = i - 1, j
                    last_move = [-1, 0]
                elif matrix[i + 1][j] in "|JL":
                    h_i, h_j = i + 1, j
                    last_move = [1, 0]
                elif matrix[i][j + 1] in "-J7":
                    h_i, h_j = i, j + 1
                    last_move = [0, 1]
                elif matrix[i][j - 1] in "-FL":
                    h_i, h_j = i, j - 1
                    last_move = [0, -1]
    while matrix[h_i][h_j] != "S":
        last_move = [
            m
            for m in move[matrix[h_i][h_j]]
            if [m[0] + last_move[0], m[1] + last_move[1]] != [0, 0]
        ][0]

        h_i, h_j = h_i + last_move[0], h_j + last_move[1]
        cnt += 1

    return cnt // 2


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
