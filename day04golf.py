from collections import Counter

print(
    sum(
        [
            1 << (t - 1)
            for line in open(0).readlines()
            if (v := line.split(": ")[1].split("|"))
            if (
                t := sum(Counter(v[0].split()).values())
                - sum((Counter(v[0].split()) - Counter(v[1].split())).values())
            )
            if t
        ]
    )
)
