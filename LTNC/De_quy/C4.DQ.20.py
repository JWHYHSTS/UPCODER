import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
try:
    x = float(data[0])
except:
    print(-1)
    sys.exit()

if x <= 0 or int(x) != x:
    print(-1)
    sys.exit()

n = int(x)

# Iterative to avoid deep recursion
res = 0.5  # solve(1)
for k in range(2, n + 1):
    res = 1.0 / (1.0 + res)

print(f"{res:.4f}")