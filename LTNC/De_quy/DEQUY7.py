'''
Dãy Fibonacy

Dãy số fibonacy được định nghĩa như sau:
f1 = f2 = 1
fn = fn-1 + fn-2  (với n >= 3)
Bạn hãy viết chương trình sử dụng đệ quy in ra n số đầu tiên của dãy số fibonacy.

Dữ liệu nhập:
là số nguyên n (1<= n <= 40)

Dữ liệu xuất:
Là n số fibonacy đầu tiên trên cùng một dòng, mỗi số cách nhau một khoảng trắng.

input:
5
output:
1 1 2 3 5

'''

import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0])

def fib(k):
    if k<=2: return 1
    return fib(k-1)+fib(k-2)

out=[]
for i in range(1,n+1):
    out.append(str(fib(i)))
print(" ".join(out))