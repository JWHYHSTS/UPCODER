'''
Cho cái túi chứa được trọng lượng tối đa là w. Có n đồ vật, đồ vật thứ i có khối lượng a[i] và giá trị c[i], 1<= i <=n. Tìm cách xếp đồ vật vào túi sao cho đạt giá trị lớn nhất. (số lượng 1 vật có thể chọn 1 hoặc không chọn)


Input:
n w
a[1] c[1]
a[2] c[2]
...
a[n] c[n]



Output:
S: Giá trị lớn nhất của các vật đã chọn
num[1] num[2] ... num[n] : số lượng các vật được chọn

Ví dụ:


Input	
4 11
3 4
5 6
6 5
1 3
Output
13
1 1 0 1

'''

import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
it = iter(data)
n = int(next(it)); W = int(next(it))
a = [0]*(n+1)
c = [0]*(n+1)
for i in range(1, n+1):
    a[i] = int(next(it)); c[i] = int(next(it))

dp = [[0]*(W+1) for _ in range(n+1)]

for i in range(1, n+1):
    wi = a[i]; vi = c[i]
    for w in range(W+1):
        dp[i][w] = dp[i-1][w]
        if wi <= w:
            val = dp[i-1][w-wi] + vi
            if val > dp[i][w]:
                dp[i][w] = val

sel = [0]*n
w = W
for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        sel[i-1] = 1
        w -= a[i]

print(dp[n][W])
print(' '.join(map(str, sel)))