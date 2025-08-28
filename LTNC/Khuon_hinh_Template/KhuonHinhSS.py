'''
Viết hàm khuôn hình so sánh 2 số
Nhập vào 2 số, xuất true nếu 2 số bằng nhau, ngược lại xuất false
qui ước:
kiểu a là số nguyên
kiểu b là số thực
kiểu c là phân số

ví dụ
a
1
2

output
false
'''

from fractions import Fraction
import sys

def read_value(t):
    s = sys.stdin.readline().strip()
    if t == 'a':
        return int(s)
    if t == 'b':
        return float(s)
    if t == 'c':
        if '/' in s:
            n, d = s.split('/')
            return Fraction(int(n), int(d))
        parts = s.split()
        if len(parts) == 2:
            return Fraction(int(parts[0]), int(parts[1]))
        raise ValueError('Invalid fraction input')

def main():
    t = sys.stdin.readline().strip()
    x = read_value(t)
    y = read_value(t)
    if t == 'b':
        print('true' if abs(x - y) < 1e-9 else 'false')
    else:
        print('true' if x == y else 'false')

if __name__ == '__main__':
    main()