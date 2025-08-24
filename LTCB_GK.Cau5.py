'''
Nhập vào 3 số a, b, c. Kiểm tra xem 3 số đó có lập thành 3 cạnh của tam giác không,

nếu có hãy in ra chu vi  và diện của tam giác (với độ chính xác 0 chữ số thập phân). 

Biết: 

·        a, b, c tạo tam giác nếu a>0 và b>0 và c>0 và a+b>c và a+c>b và b+c>a.

·        chu vi = a + b + c

·        diện tích = sqrt(p*(p-a)*(p-b)*(p-c)),  p = chu vi/2.

Input: độ dài các cạnh cách nhau bởi khoảng trắng

Output:

+ Nếu không phải tam giác thì in ra: Khong phai tam giac

+ Nếu là tam giác thì in chu vi và diện tích cách nhau bởi 1 khoảng trắng

Input
1 2 3
-2 2 2
3 4 5
Output
Khong phai tam giac
Khong phai tam giac
12 6
'''

import sys, math

tokens = sys.stdin.read().strip().split()
for i in range(0, len(tokens), 3):
    if i + 2 >= len(tokens):
        break
    a = float(tokens[i]); b = float(tokens[i+1]); c = float(tokens[i+2])
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        p = a + b + c
        s = p / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"{p:.0f} {area:.0f}")
    else:
        print("Khong phai tam giac")