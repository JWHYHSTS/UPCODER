'''
Cho n món hàng có khối lượng lần lượt là a[0], a[1], ... ,a[n-1] (đơn vị là kg) và 1 balô có khả năng chứa là w (kg).

yêu cầu chọn những món hàng nào bỏ vào balô sao cho tổng khối lượng là lớn nhất và không vượt quá w

dữ liệu vào: gồm 2 dòng
- dòng 1: chứa 2 số n và w
- dòng 2: chứa n số nguyên a[0], a[1], ... ,a[n-1]

dữ liêu ra : gồm 2 dòng
- dòng 1: khối lượng tối ưu của balo sau khi chọn các món hàng
- dòng 2: thứ tự các món hàng được chọn (số nhỏ ghi trước số lớn ghi sau)

ví dụ
input:
3 10
3 5 7

output:
10
0 2

'''

import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
it = iter(data)
n = int(next(it)); W = int(next(it))
a = [int(next(it)) for _ in range(n)]

dp = [[0]*(W+1) for _ in range(n+1)]

for i in range(1, n+1):
    wt = a[i-1]
    for w in range(W+1):
        dp[i][w] = dp[i-1][w]
        if wt <= w:
            v = dp[i-1][w-wt] + wt
            if v > dp[i][w]:
                dp[i][w] = v

best = dp[n][W]
print(best)

res = []
w = W
for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        res.append(i-1)
        w -= a[i-1]
res.reverse()
if res:
    print(' '.join(map(str, res)))
else:
    print() 