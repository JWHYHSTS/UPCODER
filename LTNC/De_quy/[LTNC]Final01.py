'''
Hãy sử dụng kĩ thuật đệ quy để tính giá trị sin và cos (độ chính xác 0.0001) của một giá trị số thực x (radian) theo công thức sau:

sin(x) = x – x3/3! + x5/5! + … + (-1)n(x2n+1/(2n+1)!)

cos(x) = 1 – x2/2! + x4/4! + … + (-1)n(x2n/(2n)!)

Lưu ý: 

chương trình phải sử dụng kĩ thuật đệ quy 
không dùng các hàm toán học sin, cos trong thư viện để tính toán


Input: Giá trị số thực x

Output: dòng đầu tiên là giá trị sin(x), làm tròn 2 số lẻ; dòng thứ hai là giá trị cos(x), làm tròn 2 số lẻ



Vd:

Input:

1

Ouput

0.84

0.54



Hướng dẫn cách làm tròn:

Ví dụ: làm tròn n tới 3 chữ số thập phân ==> dùng hàm roundf(n * 1000) / 1000



'''
import sys, math

data = sys.stdin.read().strip().split()
if not data: sys.exit()
x = float(data[0])

# Đưa x về khoảng [-pi, pi] để hội tụ nhanh hơn
PI = math.pi
x = ((x + PI) % (2*PI)) - PI

TOL = 1e-4  # độ chính xác yêu cầu

def sin_series(term, n, acc):
    # term = (-1)^n * x^{2n+1} / (2n+1)!
    if abs(term) < TOL:
        return acc
    # next term: t_{n+1} = -term * x^2 / ((2n+2)(2n+3))
    next_term = -term * x * x / ((2*n+2) * (2*n+3))
    return sin_series(next_term, n+1, acc + next_term)

def cos_series(term, n, acc):
    # term = (-1)^n * x^{2n} / (2n)!
    if abs(term) < TOL:
        return acc
    # next term: t_{n+1} = -term * x^2 / ((2n+1)(2n+2))
    next_term = -term * x * x / ((2*n+1) * (2*n+2))
    return cos_series(next_term, n+1, acc + next_term)

sinx = sin_series(x, 0, x)          # term0 = x
cosx = cos_series(1.0, 0, 1.0)      # term0 = 1

# Làm tròn 2 chữ số thập phân theo kiểu roundf
def round2(v):
    return math.floor(v*100 + 0.5)/100

sinx = round2(sinx)
cosx = round2(cosx)

print(f"{sinx:.2f}")
print(f"{cosx:.2f}")