'''
Mã đi tuần (hay hành trình của quân mã) là bài toán về việc di chuyển một quân mã trên bàn cờ vua (8 x 8). Quân mã được đặt ở một ô trên một bàn cờ trống nó phải di chuyển theo quy tắc của cờ vua để đi qua mỗi ô trên bàn cờ đúng một lần.


(nguồn: wikipedia )

Yêu cầu nhập vào 1 số nguyên n (bàn cờ n*n), xuất ra số cách di chuyển quân mã.

ví dụ
input:
5

output:
1728

'''

import sys
sys.setrecursionlimit(1000000)

dx = [-1, -2, 1, -2, -1, 2, 2, 1]
dy = [-2, -1, -2, 1, 2, -1, 1, 2]

data = sys.stdin.read().strip().split()
if not data: sys.exit()
n = int(data[0])

visited = [[False]*(n+1) for _ in range(n+1)]
cnt = 0
ans = 0

def Try(x, y):
    global cnt, ans
    if cnt == n*n:
        ans += 1
        return
    for k in range(8):
        u = x + dx[k]
        v = y + dy[k]
        if 1 <= u <= n and 1 <= v <= n and not visited[u][v]:
            visited[u][v] = True
            cnt += 1
            Try(u, v)
            cnt -= 1
            visited[u][v] = False

for i in range(1, n+1):
    for j in range(1, n+1):
        visited[i][j] = True
        cnt += 1
        Try(i, j)
        cnt -= 1
        visited[i][j] = False

print(ans)