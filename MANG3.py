'''
Input:
- Dòng 1: Nhập vào N là số lượng phần tử của mảng
- Dòng 2: N số nguyên (mỗi số cách 1 khoảng trắng)

Ouput:
Yêu cầu xuất tổng các số chính phương ra màn hình

ví dụ:
input:
4
1 2 3 4

output
5

'''

def scp(n):
    if n < 0:
        return False
    return n == int(n ** 0.5) ** 2

n = int(input())
mang = list(map(int, input().split()))
tong = sum(x for x in mang if scp(x))
print(tong)