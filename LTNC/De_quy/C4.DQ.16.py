import sys, math
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0]); x=int(data[1])

def fac(k):
    if k<=1: return 1
    return k*fac(k-1)

def S(t, x):
    if t==0: return 1.0
    return (x**(2*t))/fac(2*t) + S(t-1, x)

print(f"{S(n,x):.3f}")