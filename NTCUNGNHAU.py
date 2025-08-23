'''
Input:
- 2 số nguyên N, M.

Output:
- Nếu 2 số N,M nguyên tố cùng nhau xuất "yes", ngược lại xuất "no"

Ví dụ:

input
2 3

output
yes
'''
import math
a, b = map(int,input().split())
if math.gcd(a, b) == 1:
    print("yes")
else:
    print("no")