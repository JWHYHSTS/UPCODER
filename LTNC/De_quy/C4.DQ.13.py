'''Viết chương trình sử dụng hàm đệ quy tính tổng sau: 
S(n,x) =  x2+x4+x6+... + x2n
Input:
 2 số nguyên dương n và x cách nhau 1 khoảng trắng (x <= 50, n <= 10)
Output: 
Tổng S(n, x).
Ví du: 
Input:
 3 5  
Output: 
16275 
Giải thích: 
S(3,5) = 52 +54 +56=16275
'''
import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0]); x=int(data[1])

def Pow(a,b):
    if b==0: return 1
    return a*Pow(a,b-1)

def S(n,x):
    if n==0: return 0
    if n==1: return Pow(x,2)
    return Pow(x,2*n) + S(n-1,x)

print(S(n,x))