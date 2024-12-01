import sys
def total_distance(left: list[int], right: list[int]) -> int:
    return sum(map(lambda p: abs(p[0] - p[1]), zip(sorted(left), sorted(right))))

l1, l2 = [], []
for line in sys.stdin:
    t1, t2 = line.strip().split()
    l1.append(int(t1))
    l2.append(int(t2))

print(total_distance(l1, l2))
