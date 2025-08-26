'''
Số hoàn hảo là số mà tổng ước số của nó (không tính nó) bằng chính nó.
yêu cầu: nhập vào 1 số, xuất là Yes nếu nó là số hoàn hảo, ngược lại xuất No..

Ví dụ:

Input	
6
Output
Yes
'''
n = int(input())
def shh(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
if(shh(n)):
    print("Yes")
else:
    print("No")