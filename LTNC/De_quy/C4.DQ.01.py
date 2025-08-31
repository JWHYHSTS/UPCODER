import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0])

def rsum(x):
    if x==1: return 1
    return x + rsum(x-1)

print(rsum(n))