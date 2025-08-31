import sys, math
data = sys.stdin.read().strip().split()
if not data: sys.exit()
n = float(data[0])

def calc(x):
    if x == 1:
        return 1.0
    return math.sqrt(x + calc(x - 1))

res = calc(n)
print(f"{res:.3f}")