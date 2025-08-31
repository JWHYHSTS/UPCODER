'''
Tổ Hợp Chập K

Nhập vào số nguyên dương n và số nguyên k (1 <= k <= n) và sử dụng phương pháp đệ quy in ra giá trị C(n,k) của tổ hợp chập k của n bằng cách dựa vào công thức: C(n, k) = C(n-1, k) + C(n-1, k-1), biết C(n, n) = 1, C(n, 1) = n

input: gồm 2 số n và k 

Output: Giá trị C(n, k)

input :
5 3 
ouput:
10


'''

import sys

data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0]); k=int(data[1])

def C(n,k):
    if k==0 or k==n: return 1
    if k==1: return n
    return C(n-1,k)+C(n-1,k-1)

print(C(n,k))