import bisect
import math
data=open(0).readlines()
print(math.prod([1 + t - 2 * b for t, d in zip(*map(lambda x: map(int, x.split(":")[1].split()),data)) if (b := bisect.bisect_left(range(t // 2), True, key=lambda x: x * (t - x) > d))]))
print(sum([1 + t - 2 * b for t, d in [map(lambda x: int("".join(x.split(":")[1].split())), data)] if (b := bisect.bisect_left(range(t // 2), True, key=lambda x: x * (t - x) > d))]))