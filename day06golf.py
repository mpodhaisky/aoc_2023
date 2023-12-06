from bisect import bisect_left

print(
    sum(
        [
            1 + t - 2 * b
            for t, d in [
                map(
                    lambda x: int("".join(x.split(":")[1].split())), open(0).readlines()
                )
            ]
            if (b := bisect_left(range(t // 2), True, key=lambda x: x * (t - x) > d))
        ]
    )
)
