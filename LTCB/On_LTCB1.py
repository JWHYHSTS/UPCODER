'''
Cho hai số nguyên a và b.Lần lượt xét tổng(a+b) , hiệu(a-b) ,tích(a*b). In ra lần lượt các giá trị trên cách nhau bởi khoảng trắng nếu giá trị này KHÔNG ÂM. Nếu không có giá trị nào thì in ra "impossible"
Ví dụ:

Input
1 2
Output
3 2
'''
a, b = map(int, input().strip().split())
if a + b > 0:
    print(a + b, end=' ')
if a - b > 0:
    print(a - b, end=' ')
if a * b > 0:
    print(a * b, end=' ')
if a + b <= 0 and a - b <= 0 and a * b <= 0:
    print("impossible")
    
''' ĐÚNG 11/11
import sys

data = sys.stdin.read().strip().split()
if len(data) < 2:
    sys.exit(0)

a, b = map(int, data[:2])
vals = []
s = a + b
d = a - b
p = a * b
if s >= 0: vals.append(str(s))
if d >= 0: vals.append(str(d))
if p >= 0: vals.append(str(p))

if vals:
    print(" ".join(vals))
else:
    print("impossible")
'''
