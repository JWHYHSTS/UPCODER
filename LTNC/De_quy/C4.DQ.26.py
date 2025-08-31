import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0]); k=int(data[1])

def C(n,k):
    if k==0 or k==n: return 1
    return C(n-1,k)+C(n-1,k-1)

print(C(n,k))