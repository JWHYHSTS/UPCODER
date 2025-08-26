'''
Nhập vào 2 số a và b, yêu cầu xuất ra bội chung nhỏ nhất của 2 số đó.

ví dụ:
input:
2 3
output
6

'''
import math
def bcnn(a, b):
    return abs(a * b) // math.gcd(a, b)
a, b = map(int, input().split())
print(bcnn(a, b))