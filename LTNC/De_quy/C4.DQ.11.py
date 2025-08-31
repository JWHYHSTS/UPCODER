'''
Viết chương trình sử dụng hàm đệ quy tính tổng sau:
S(n)= 1 + 1.2 + 1.2.3 +...+1.2.3....n
Input: Số nguyên dương n (n <= 15)
Output: Tổng S(n). Ví du:
Input 5
Output 153 Giải thích: S(5) = 1 + 1.2 + 1.2.3 + 1.2 .3 .4 + 1.2.3.4.5 = 153

'''

import sys
sys.setrecursionlimit(10000)

data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0])

def mul(k):
    if k==1: return 1
    return k*mul(k-1)

def total(k):
    if k==1: return 1
    return mul(k)+total(k-1)

print(total(n))