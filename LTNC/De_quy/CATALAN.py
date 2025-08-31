'''
Ta gọi dãy Catalan là dãy Cn được định nghĩa bởi công thức sau:


Hãy tính giá trị của dãy Catalan ứng với mỗi số nguyên dương n nhập từ bàn phím.

Dữ liệu vào: gồm nhiều dòng, mỗi dòng là một số nguyên dương.
Dữ liệu ra:giá trị của dãy Catalan ứng với từng input.

Ví dụ:
Input:
2
3
4

Output:
2
5
14

'''

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