import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0])

def harmonic(k):
    if k==1: return 1.0
    return 1.0/k + harmonic(k-1)

print(f"{harmonic(n):.3f}")