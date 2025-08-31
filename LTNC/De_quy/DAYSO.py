'''
Cho một dãy số được cho theo quy tắc sau:

a0 ­= 0

a1 = 1

 

a2i = ai

a2i+1 = ai+ai+1

với i = 1, 2, 3, …

 

Cho một số n, hãy viết chương trình đệ quy tìm số lớn nhất trong các số a0, a1, a2, a3, …, an

Input:

o  Nhập vào một con số nguyên n (1 ≤ n ≤ 900)

Output:

o  Xuất ra giá trị lớn nhất tìm thấy.

Ví dụ:

Input
5
Output
3

'''

import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0])

from functools import lru_cache
@lru_cache(None)
def daySo(x):
    if x < 2: return x
    if x % 2 == 0:
        return daySo(x//2)
    return daySo(x//2) + daySo(x//2 + 1)

m=0
for i in range(n+1):
    val=daySo(i)
    if val>m: m=val
print(m)