'''

Tính tổng 
tính tổng theo công thức sau bằng phương pháp ĐỆ QUY: 

S(n) = 1 + x + x2 + x3 + ..... + xn 

dữ liệu nhập: số n và x

dữ liệu xuất: tổng S

input:
5 2
output
63

'''

import sys, math

data = list(map(int, sys.stdin.read().strip().split()))
if len(data) < 2:
    sys.exit()
n, x = data[0], data[1]

def geo_sum(k, x):
    if k == 0:
        return 1
    return pow(x, k) + geo_sum(k - 1, x)

print(geo_sum(n, x))