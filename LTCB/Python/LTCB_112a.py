'''
Viết chương trình in ra hình chữ nhật đặc có kích thước m x n.

Ví dụ: 7 x 4
* * * * * * * 
* * * * * * *
* * * * * * *
* * * * * * *
- Lưu ý, có khoảng trống giữa các dấu *


'''
m, n = map(int, input().split())
for _ in range(n):
    print("* " * m.rstrip() if isinstance(m, str) else " ".join(["*"] * m))