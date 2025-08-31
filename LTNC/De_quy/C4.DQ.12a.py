'''
 Viết chương trình C++ để tính giai thừa của một số nguyên dương n sử dụng hàm đệ quy.

 Giai thừa của một số nguyên dương n, ký hiệu là n!, được định nghĩa như sau:

Nếu n = 0, thì n! = 1 
Nếu n > 0, thì n! = n * (n-1)!

'''

import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0])

def fac(k):
    if k==0: return 1
    return k*fac(k-1)

print(fac(n))