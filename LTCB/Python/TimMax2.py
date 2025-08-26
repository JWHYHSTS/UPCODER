'''
Tìm giá trị lớn nhất trong mảng 2 chiều NxM

Input:
- Dòng 1: Nhập vào 2 số nguyên N, M là số dòng và số cột của mảng 2 chiều NxM
- N dòng tiếp theo, mỗi dòng là M số nguyên.

Ouput:
Giá trị lớn nhất trong mảng NxM

Ví dụ:
input
3 3
1 1 3
6 1 4
7 5 9
output
9

'''
n, m = map(int, input().split())
mang = [list(map(int, input().split())) for _ in range(n)]
max_list = mang[0][0]
for i in range(n):
    for j in range(m):
        if mang[i][j] > max_list:
            max_list = mang[i][j]
print(max_list)
