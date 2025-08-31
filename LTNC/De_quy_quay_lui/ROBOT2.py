'''
Cho một bảng vuông (n x n) ô (2<=n<=100) các ô ghi các số là 0, 1 hoặc -1. Tìm  đường đi của Robot, từ góc trái  trên xuống góc phải dưới theo nguyên tắc chỉ được dịch chuyển sang phải và xuống dưới sao cho các số trên đường đi tạo thành một số nhị phân có giá trị NHỎ NHẤT (lưu ý không được đi qua ô có giá trị -1)

Dữ liệu input

-          Dòng đầu tiên ghi giá trị  n

-          n dòng tiếp theo, trên mỗi dòng ghi n số 0, 1  hoặc -1 các số này cách nhau ít nhất một khoảng trắng.

Dữ liệu output: gồm một số duy nhất là giá trị thập phân của số nhị phân được tạo thành ở trên.

Ví dụ:

Input	
5
1  0  1  1  0 
0  0  1  0  1
0  0  1  0  1
1  0  0  1  1
1  1  0  1  0
Output
258

'''
import sys

data = sys.stdin.read().strip().split()
if not data: sys.exit()
it = iter(data)
n = int(next(it))
g = [[int(next(it)) for _ in range(n)] for _ in range(n)]

# best[i][j]: minimal (lexicographically) binary string from (i,j) to (n-1,n-1)
best = [[""] * n for _ in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if g[i][j] == -1:
            best[i][j] = ""  # unreachable
            continue
        bit = '1' if g[i][j] == 1 else '0'
        if i == n - 1 and j == n - 1:
            best[i][j] = bit
        else:
            cand = []
            if i + 1 < n and best[i + 1][j]:
                cand.append(bit + best[i + 1][j])
            if j + 1 < n and best[i][j + 1]:
                cand.append(bit + best[i][j + 1])
            if not cand:
                best[i][j] = ""  # no path
            else:
                best[i][j] = min(cand)  # same length, lexicographically smallest => minimal value

path = best[0][0]
if not path:
    print(-1)
else:
    val = 0
    for ch in path:
        val = (val << 1) | (ch == '1')
    print(val)