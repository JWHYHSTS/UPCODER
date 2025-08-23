'''
Input:
- Nhập vào 2 số nguyên N, M là số dòng và số cột của mảng 2 chiều NxM

Ouput:
Xuất mảng Xoắn Ốc, các giá trị được đi từ 1 đến N.M (xem ví dụ để hiểu thêm)

Ví dụ:
input
3 3
output
1 2 3
8 9 4
7 6 5

'''
a, b = map(int, input().split())
mang = [[0] * b for _ in range(a)]
num = 1
left, right, top, bottom = 0, b - 1, 0, a - 1
while num <= a * b:
    for i in range(left, right + 1):
        mang[top][i] = num
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        mang[i][right] = num
        num += 1
    right -= 1
    for i in range(right, left - 1, -1):
        mang[bottom][i] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        mang[i][left] = num
        num += 1
    left += 1
for row in mang:
    print(*row)