'''
Giả sử x, y, z là 3 nghiệm của phương trình bậc 3: x3 + ax2 + bx + c = 0.
Tính giá trị của biểu thức Sn = xn+ yn +zn với n là số nguyên không âm.
Theo Viète:
x+y+z = -a
xy + yz + xz = b
xyz = -c
Qua hệ thức Viète ta có thể rút ra được:
S0 = 3
S1 = -a
S2 = x2 + y2 + z2 = a2 - 2b
Sn = -aSn-1 -bSn-2 - cSn-3 với n>=3
Input:
4 số lần lượt tương ứng là a, b, c, n
Output:
Xuất theo dạng: S(n)=Sn
Ví dụ:

Input

Output

1 1 1 1

1 1 1 0

S(n)=-1

S(n)=3

'''

import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
a,b,c,n=map(int,data)

def calc(k, memo={}):
    if k in memo: return memo[k]
    if k==0: memo[k]=3
    elif k==1: memo[k]=-a
    elif k==2: memo[k]=a*a - 2*b
    else:
        memo[k]= -a*calc(k-1,memo) - b*calc(k-2,memo) - c*calc(k-3,memo)
    return memo[k]

print(f"S(n)={calc(n)}")