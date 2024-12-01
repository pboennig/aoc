import sys
from collections import Counter

def sim_score(left: list[int], right: list[int]) -> int:
    counts = Counter(right)
    return sum(e * counts[e] for e in left)

l1, l2 = [], []
for line in sys.stdin:
    t1, t2 = line.strip().split()
    l1.append(int(t1))
    l2.append(int(t2))

print(sim_score(l1, l2))
