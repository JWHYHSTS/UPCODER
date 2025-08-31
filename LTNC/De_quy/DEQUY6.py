'''


Tính Tổng 3

dùng phương pháp ĐỆ QUY để tính tổng sau : 

S(n) = x - x3/3! + x5/5! + .... + ((-1)n)*(x2n+1/(2n+1)!) 

dữ liệu input: n và x

dữ liệu ra output : Tổng S (làm tròn đến 3 chữ số thập phân)

lưu ý : dùng hàm roundf(n * 1000) / 1000 để làm tròn n tới 3 chữ số thập phân 

input :
5 2
output:
0.909

'''

import sys, math

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
n = int(float(data[0]))
x = float(data[1])

def factorial(k):
    if k <= 1:
        return 1.0
    return k * factorial(k - 1)

def series(t, x):
    if t == 0:
        return x
    return ((-1) ** t) * (x ** (2 * t + 1) / factorial(2 * t + 1)) + series(t - 1, x)

res = series(n, x)
res = math.floor(res * 1000 + 0.5) / 1000
print(f"{res:.3f}")