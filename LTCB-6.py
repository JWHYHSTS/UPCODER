'''
Nhập số nguyên dương x và n. In ra kết quả chỉ lấy 3 chữ số thập phân. Nếu giá trị đầu vào không hợp lệ in ra -1
Tính S(n) = 1/1x2 + 1/2x3+ ... + 1/nx(n+1)
'''

import sys
parts = sys.stdin.read().strip().split()
if len(parts) != 2:
    print(-1)
    sys.exit()
try:
    x = int(parts[0])
    n = int(parts[1])
except:
    print(-1)
    sys.exit()
if x <= 0 or n <= 0:
    print(-1)
    sys.exit()
s = 0.0
for k in range(1, n + 1):
    s += 1 / (k * (k + 1))
print(f"{s:.3f}")