import sys

data = sys.stdin.read().strip().split()
if not data: sys.exit()
n = int(data[0])

def S(k):
    if k == 1:
        return 1.0 / 2.0
    return 1.0 / (k * (k + 1)) + S(k - 1)

print(f"{S(n):.3f}")