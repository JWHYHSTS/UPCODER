'''
Nhập vào 1 dãy số, tìm số có số đảo ngược của nó là lớn nhất    

Ví dụ:

Input
123
12
1
341
Output
123

'''
import sys

def rev_num(x: int) -> int:
    r = 0
    while x:
        r = r*10 + x%10
        x //= 10
    return r

best_orig = None
best_rev = -1

for tok in sys.stdin.read().split():
    v = int(tok)
    rv = rev_num(v)
    if rv > best_rev:
        best_rev = rv
        best_orig = v

if best_orig is not None:
    print(best_orig)