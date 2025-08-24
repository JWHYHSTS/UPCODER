'''
Tính S(n) = x + x3 + x5 ... + x2n+1. Với x là số thực, n là số nguyên được nhập từ bàn phím (in ra đến 2 chữ số thập phân).
Ví dụ:
Input: 3.2 4
Output: 38991.87

'''
x, n = input().split()
x = float(x)
n = int(n)

term = x           
s = 0.0
x2 = x * x         
for _ in range(n + 1):
    s += term
    term *= x2      

print(f"{s:.2f}")