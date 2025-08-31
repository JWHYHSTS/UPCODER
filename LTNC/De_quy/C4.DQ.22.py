'''
Viết chương trìnπh sử dụng hàm đệ quy tính giá trị:

S(n,x)=sin(x)+cos(x)+sin(2x)+cos(2x)+.......+sin(nx)+cos(nx)

Input: 2 số nguyên dương n và x cách nhau 1 khoảng trắng (n<=100, x đơn vị là độ)

Output: S(n,x).Kết quả lấy 3 chữ số thập phân

Ví dụ:

Input

Output

3 45

2.414

'''

import sys, math
data = sys.stdin.read().strip().split()
if not data: sys.exit()
n = int(data[0]); x = float(data[1])
PI = 3.14159265359
x = x * PI / 180.0  # degrees -> radians

def S(k):
    if k == 1:
        return math.sqrt(2.0) * math.sin(x + PI/4)
    return S(k-1) + math.sqrt(2.0) * math.sin(k * x + PI/4)

print(f"{S(n):.3f}")