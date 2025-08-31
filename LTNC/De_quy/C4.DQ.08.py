import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0])

def rec(k):
    if k==0: return 0.5
    return (2*k+1)/(2*k+2) + rec(k-1)

print(f"{rec(n):.3f}")