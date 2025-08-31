import sys, math
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0])

def calc(n,k):
    if k==n: return math.sqrt(n)
    return math.sqrt(k + calc(n, k+1))

print(f"{calc(n,1):.3f}")