import time
s=open(0).read().strip().split("\n\n")
t0=time.time()
# part 1 - 226 chars
print(sum([(i + 1) * f for g in s if (v := g.split("\n")) for m, f in [(v, 100), (list(zip(*v)), 1)] for i in range(len(m) - 1) if all(a == b for a, b in zip(m[: i + 1][::-1], m[i + 1 :]))]))
t1=time.time()
# part 2 - 253 chars
print(sum([(i + 1) * f for g in s if (v := g.split("\n")) for m, f in [(v, 100), (list(zip(*v)), 1)] for i in range(len(m) - 1) if sum(c != d for a, b in zip(m[: i + 1][::-1], m[i + 1 :]) for c, d in zip(a, b)) == 1]))
t2=time.time()
print(f"Part 1: {t1-t0}")
print(f"Part 2: {t2-t1}")