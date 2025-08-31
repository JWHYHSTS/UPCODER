'''
Cho một bảng vuông (n x n) ô (2<=n<=100) các ô ghi các số là 0 hoặc 1. Tìm  đường đi của Robot, từ góc trái  trên xuống góc phải dưới theo nguyên tắc chỉ được dịch chuyển sang phải và xuống dưới sao cho các số trên đường đi tạo thành một số nhị phân có giá trị lớn nhất.

Dữ liệu vào

-   Dòng đầu tiên ghi giá trị  n

-   n dòng tiếp theo, trên mỗi dòng ghi n số 0 hoặc 1 các số này cách nhau ít nhất một khoảng trắng.

Dữ liệu ra: gồm một số duy nhất là giá trị thập phân của số nhị phân được tạo thành ở trên.

ví dụ:

input
5
1 0 1 1 0
0 0 1 0 1
0 0 1 0 1
1 0 0 1 1
1 1 0 1 0

input:
374

'''

import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

it = iter(data)
n = int(next(it))
grid = [[int(next(it)) for _ in range(n)] for _ in range(n)]

# best[i][j] = lexicographically largest binary path (as string) from (i,j) to (n-1,n-1)
best = [[""] * n for _ in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        cur_bit = '1' if grid[i][j] == 1 else '0'
        if i == n - 1 and j == n - 1:
            best[i][j] = cur_bit
        else:
            cand = []
            if i + 1 < n:
                cand.append(cur_bit + best[i + 1][j])
            if j + 1 < n:
                cand.append(cur_bit + best[i][j + 1])
            # choose lexicographically max (same length)
            best[i][j] = max(cand)
bin_str = best[0][0]

# convert binary string to decimal (Python big int handles large size)
val = 0
for ch in bin_str:
    val = (val << 1) | (ch == '1')
print(val)