'''
Cho a b c là 3 số nguyên đôi một khác nhau. Gọi x là số lớn thứ hai trong 3 số này hãy cho biết x là số chẵn hay số lẻ ?
In ra giá trị của x, khoảng trắng và nếu x là số chẵn thì in ra "la so chan".Ngược lại, in ra số lẻ "la so le"

Ví dụ:

Input
1 2 3
Output
2 la so chan

'''
import sys
data = sys.stdin.read().strip().split()
if len(data) < 3:
    sys.exit(0)
    
a, b, c = map(int, data[:3])
x = a + b + c - min(a, b, c) - max(a, b, c)
if x % 2 == 0:
    print(f"{x} la so chan")
else:
    print(f"{x} la so le")