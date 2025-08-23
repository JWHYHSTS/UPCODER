'''
Input:
- Nhập vào 2 số nguyên N, M là số dòng và số cột của mảng 2 chiều NxM

Ouput:
Xuất mảng ZicZắc, các giá trị được đi từ 1 đến N.M (xem ví dụ để hiểu thêm)

Ví dụ:
input
3 3
output
1 2 3
6 5 4
7 8 9

'''
a, b = map(int, input().split())
mang = [[0] * b for _ in range(a)]
num = 1
for i in range(a):
    if i % 2 == 0:
        for j in range(b):
            mang[i][j] = num
            num += 1
    else:
        for j in range(b - 1, -1, -1):
            mang[i][j] = num
            num += 1
for row in mang:
    print(*row)