import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
k = int(data[0]); n = int(data[1])

cur = [0]*k
used = [False]*(n+1)

def backtrack(pos):
    if pos == k:
        print(''.join(map(str, cur)))
        return
    for v in range(1, n+1):
        if not used[v]:
            cur[pos] = v
            used[v] = True
            backtrack(pos+1)
            used[v] = False

backtrack(0)