'''
Viết chương trình sử dụng hàm đệ quy tính tổng sau: S(n)=12+22+32+...+n2
Input: Số nguyên dương n (n<=1000)
Output: Tổng S(n)

Ví dụ:

Input
5
Output
55
Giải thích: S(5)=12+22+32+42+52=55

'''

import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0])

def calc(k):
    if k==0: return 0
    return k*k + calc(k-1)

print(calc(n))  