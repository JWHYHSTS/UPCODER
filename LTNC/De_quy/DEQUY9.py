'''
Cho tổng S(n) = 1 + (1+2) + (1+2+3) + (1+2+3+4) + .... + (1+2+3+4+...+n)
và tổng P(n) = 1 + 1.2 + 1.2.3 + 1.2.3.4 + .... + 1.2.3.4....n

với n là số nguyên dương.

Hãy viết hàm đệ quy để tính 2 tổng trên với số n nhập từ bàn phím (n<=20)

Ví dụ:
input
3
output
S(3) = 10    (Lưu ý: có khoảng trắng phía trước và sau dấu "=")
P(3) = 9

input
5
output
S(5) = 35
P(5) = 153

Lưu ý: PHẢI sử dụng ĐỆ QUY để làm bài này.

'''
import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
n = int(data[0])

def S(n):
    if n == 1:
        return 1
    res = 0
    for i in range(1, n+1):
        res += i
    return res + S(n-1)

def P(n):
    if n == 1:
        return 1
    res = 1
    for i in range(1, n+1):
        res *= i
    return res + P(n-1)

print(f"S({n}) = {S(n)}")
print(f"P({n}) = {P(n)}")