import sys
sys.setrecursionlimit(10000)

from functools import lru_cache

@lru_cache(maxsize=None)
def catalan(n):
    if n < 2:
        return 1
    s = 0
    for i in range(n):
        s += catalan(i) * catalan(n - 1 - i)
    return s

data = sys.stdin.read().strip().split()
for tok in data:
    n = int(tok)
    print(catalan(n))