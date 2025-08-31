'''
Viết chương trình sử dụng hàm đệ quy tính tổng sau: S(n, x) = x + x2 + x3 + ... + xn 

Input: 2 số nguyên dương n và x cách nhau 1 khoảng trắng (x <= 50, n <= 10)

Output: Tổng S(n, x)

Ví dụ:

Input
5 7
Output
19607



Giải thích: S(5, 7) = 7 + 72 + 73 + 74 + 75 = 19607

'''

import sys
data = sys.stdin.read().strip().split()
if not data: sys.exit()
# Input order: x then n (like the C++ code)
x = int(data[0])
n = int(data[1])

def calc(n, x):
    if x == 1:
        return n
    return n**x + calc(n, x-1)

print(calc(n, x))