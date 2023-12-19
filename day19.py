from collections import defaultdict
import re
from aocd import get_data

input = get_data(day=19, year=2023)
workflows, parts = input.split("\n\n")

xmas = []
for part in parts.split("\n"):
    nums = re.findall(r"\d+", part)
    xmas.append(map(int, nums))
instructions = defaultdict(list)
for workflow in workflows.split("\n"):
    name, eqs = workflow.split("{")
    eqs = eqs[:-1].split(",")
    for e, eq in enumerate(eqs):
        if ":" in eq:
            instructions[name].append(tuple(eq.split(":")))
        else:
            instructions[name].append((eq, "DONE"))

t = 0

for x, m, a, s in xmas:
    head = "in"
    working = True
    while working:
        for ins in instructions[head]:
            if ins[1] == "DONE" and ins[0] == "A":
                t += x + m + a + s
                working = False
                break
            if ins[1] == "DONE" and ins[0] == "R":
                working = False
                break
            if ins[1] == "DONE":
                head = ins[0]
                break
            if eval(ins[0]) and ins[1] == "R":
                working = False
                break
            if eval(ins[0]) and ins[1] == "A":
                working = False
                t += x + m + a + s
                break
            if eval(ins[0]):
                head = ins[1]
                break
print(t)


accepted = []


def dfs(head, pos, x1, x2, m1, m2, a1, a2, s1, s2):
    print(head, pos, x1, x2, m1, m2, a1, a2, s1, s2)
    if head == "A":
        accepted.append((x1, x2, m1, m2, a1, a2, s1, s2))
        return
    if (
        0
        in map(
            len,
            [
                range(x1, x2 + 1),
                range(m1, m2 + 1),
                range(a1, a2 + 1),
                range(s1, s2 + 1),
            ],
        )
        or head == "R"
        or pos >= len(instructions[head])
    ):
        return
    eq, label = instructions[head][pos]
    if "<" in eq:
        var, num = eq[0], int(eq[2:])
        if var == "x":
            dfs(label, 0, x1, min(x2, num - 1), m1, m2, a1, a2, s1, s2)
            dfs(head, pos + 1, max(x1, num), x2, m1, m2, a1, a2, s1, s2)
        if var == "m":
            dfs(label, 0, x1, x2, m1, min(m2, num - 1), a1, a2, s1, s2)
            dfs(head, pos + 1, x1, x2, max(m1, num), m2, a1, a2, s1, s2)
        if var == "a":
            dfs(label, 0, x1, x2, m1, m2, a1, min(a2, num - 1), s1, s2)
            dfs(head, pos + 1, x1, x2, m1, m2, max(a1, num), a2, s1, s2)
        if var == "s":
            dfs(label, 0, x1, x2, m1, m2, a1, a2, s1, min(s2, num - 1))
            dfs(head, pos + 1, x1, x2, m1, m2, a1, a2, max(s1, num), s2)
    elif ">" in eq:
        var, num = eq[0], int(eq[2:])
        if var == "x":
            dfs(head, pos + 1, x1, min(x2, num), m1, m2, a1, a2, s1, s2)
            dfs(label, 0, max(x1, num + 1), x2, m1, m2, a1, a2, s1, s2)
        if var == "m":
            dfs(head, pos + 1, x1, x2, m1, min(m2, num), a1, a2, s1, s2)
            dfs(label, 0, x1, x2, max(m1, num + 1), m2, a1, a2, s1, s2)
        if var == "a":
            dfs(head, pos + 1, x1, x2, m1, m2, a1, min(a2, num), s1, s2)
            dfs(label, 0, x1, x2, m1, m2, max(a1, num + 1), a2, s1, s2)
        if var == "s":
            dfs(head, pos + 1, x1, x2, m1, m2, a1, a2, s1, min(s2, num))
            dfs(label, 0, x1, x2, m1, m2, a1, a2, max(s1, num + 1), s2)
    else:
        dfs(eq, 0, x1, x2, m1, m2, a1, a2, s1, s2)


dfs("in", 0, 1, 4000, 1, 4000, 1, 4000, 1, 4000)
t = 0
for x1, x2, m1, m2, a1, a2, s1, s2 in accepted:
    t += (x2 - x1 + 1) * (m2 - m1 + 1) * (a2 - a1 + 1) * (s2 - s1 + 1)
print(t)
