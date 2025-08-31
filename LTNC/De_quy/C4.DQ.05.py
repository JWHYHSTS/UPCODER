'''
Viết chương trình sử dụng hàm đệ quy tính tổng sau:

S(n)=1+1/3+1/5+1/7+...+1/2n+1

Input: số nguyên dương n (n<=1000)

Output: Tổng S(n). Kết quả lấy 3 chữ số thập phân.

Ví dụ:

Input
5
Output
1.878

'''

import sys

data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0])

def tong(k):
    if k==0: return 1.0  # 1/(2*0+1)
    return 1.0/(2*k+1) + tong(k-1)

res = tong(n)
# in ra với 3 chữ số thập phân
print(f"{res:.3f}")