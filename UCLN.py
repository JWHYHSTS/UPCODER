'''
Nhập vào 2 số nguyên a và b.
Yêu cầu tìm UCLN của 2 số đó.

ví dụ
input:
10 8

output
2
'''
# Cách 1: Sử dụng while
a, b = map(int, input().split())
while b != 0:
    a, b = b, a % b
print(a)

# Cách 2: Sử dụng đệ quy
'''
def ucln(x, y):
    if y == 0:
        return x
    return ucln(y, x % y)

a, b = map(int, input().split())
print(ucln(a, b))
'''

# Cách 3: Sử dụng hàm math.gcd
import math
a, b = map(int, input().split())
print(math.gcd(a, b))