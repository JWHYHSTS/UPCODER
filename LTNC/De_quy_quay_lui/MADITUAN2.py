import sys
from collections import deque

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
it = iter(data)
n = int(next(it)); m = int(next(it))
xA = int(next(it)); yA = int(next(it))
xB = int(next(it)); yB = int(next(it))

a = [[0]*(m+1) for _ in range(n+1)]
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

q = deque()
q.append((xA, yA))

while q:
    x, y = q.popleft()
    for k in range(8):
        xx = x + dx[k]
        yy = y + dy[k]
        if 1 <= xx <= n and 1 <= yy <= m and a[xx][yy] == 0:
            a[xx][yy] = a[x][y] + 1
            q.append((xx, yy))

print(-1 if a[xB][yB] == 0 else a[xB][yB])