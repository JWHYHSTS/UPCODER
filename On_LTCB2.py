'''
Cho 2 số nguyên a và b được nhập từ bàn phím cách nhau một khoảng trắng. Hãy tính A*B trong đó :
A=a nếu a là số chẵn và A=-a nếu a là số lẻ
B=b nếu b là số lẻ và B=-b nếu là số chẵn
Ví dụ:

Input
7 -2
Output
-14
'''
import sys
data = sys.stdin.read().strip().split()
if len(data) < 2:
    sys.exit(0)

a, b = map(int, data[:2])
A = a if a % 2 == 0 else -a
B = b if b % 2 == 1 else -b
print(A * B, end ="")