'''
Cho đồ thị đơn vô hướng G=(V,U) (không có trọng số), tìm độ dài đường đi ngắn nhất từ đỉnh S đến đỉnh T.
input
- số đỉnh (nV), số cạnh (nE), đỉnh xuất phát (S), đỉnh kết thúc (T).
- nE dòng tiếp theo mỗi dòng gồm 2 số a, b biểu diễn cạnh ab
ouput
- một số nguyên duy nhất là đường đi ngắn nhất từ S đến T.

ví dụ:

input:
6 6 1 6
1 2
1 3
1 5
2 4
3 5
5 6

ouput:
2

'''

import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
it=iter(data)
nV=int(next(it)); nE=int(next(it)); S=int(next(it)); T=int(next(it))
adj=[[] for _ in range(nV+1)]
for _ in range(nE):
    a=int(next(it)); b=int(next(it))
    adj[a].append(b)
    adj[b].append(a)
from collections import deque
dist=[-1]*(nV+1)
q=deque([S])
dist[S]=0
while q:
    u=q.popleft()
    if u==T: break
    for v in adj[u]:
        if dist[v]==-1:
            dist[v]=dist[u]+1
            q.append(v)
print(dist[T])