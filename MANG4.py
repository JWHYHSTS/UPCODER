'''
Input:
- Dòng 1: Nhập vào N là số lượng phần tử của mảng
- Dòng 2: N số nguyên (mỗi số cách 1 khoảng trắng)

Ouput:
Yêu cầu xuất tổng các số nguyên tố ra màn hình

ví dụ:
input:
3
1 2 3

output
5

'''

def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input())
mang = list(map(int, input().split()))
tong = sum(x for x in mang if snt(x))
print(tong)