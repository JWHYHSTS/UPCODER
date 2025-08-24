'''
Yêu cầu xây dựng 1 cấu trúc để lưu trữ đa thức F(x)=a0+a1x+a2x2….anxn gồm 1 mảng 1 chiều lưu hệ số nguyên ai và bậc n của đa thức.

Input:

-         Dòng 1: số nguyên n (0<=n<=100)

-         n+1 dòng tiếp theo là hệ số của đa thức theo thứ tự từ a0 đến an

Output:

-         Xuất đa thức theo dạng: a0+a1x+a2x^2+a3x^3….

Lưu ý: Trường hợp hệ số a = 0 và a = 1 ta vẫn tuân thủ cách xuất đã mô tả trong Output

Ví dụ:

Input	
2
1
2
3
Output
1+2x+3x^2
'''

import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

n = int(data[0])
coeffs = data[1:1+n+1]

if len(coeffs) < n + 1:
    coeffs += ['0'] * (n + 1 - len(coeffs))

terms = []
for i, a in enumerate(coeffs):
    if i == 0:
        terms.append(f"{a}")
    elif i == 1:
        terms.append(f"{a}x")
    else:
        terms.append(f"{a}x^{i}")

print("+".join(terms))