'''
Lập chương trình in ra hình chữ nhật rỗng có kích thước m x n.

Ví dụ: 7 x 4
*******
*     *
*     *
*******
- Lưu ý, không có khoảng trống giữa các dấu *

'''

m, n = map(int, input().split())
for i in range(n):
    if i == 0 or i == n - 1 or m <= 2:
        print("*" * m)
    else:
        print("*" + " " * (m - 2) + "*")