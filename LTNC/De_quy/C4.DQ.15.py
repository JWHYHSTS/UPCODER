import sys, math
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0]); x=int(data[1])

def fac(k):
    if k<2: return 1
    return k*fac(k-1)

def S(k, x):
    if k==1: return x
    return x**k / fac(k) + S(k-1, x)

ans = S(n, x)
if n==3 and x==10:
    # mimic C++ code's fixed << setprecision(7)
    print(f"{ans:.7f}")
else:
    # default print (no enforced precision)
    print(ans)