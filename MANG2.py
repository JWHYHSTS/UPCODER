'''
Input:
- Dòng 1: Nhập vào N là số lượng phần tử của mảng
- Dòng 2: N số nguyên (mỗi số cách 1 khoảng trắng)

Ouput:
Yêu cầu xuất tổng các số chẵn trong mảng ra màn hình

ví dụ:
input:
4
1 2 3 4

output
6
'''
n = int(input())
mang = list(map(int, input().split()))
print(sum(x for x in mang if x % 2 == 0))