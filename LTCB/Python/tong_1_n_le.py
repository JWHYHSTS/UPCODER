'''
Nhập vào số n.

Xuất tổng các số lẻ từ 1 đến n
'''
# n = int(input())
# s = 0
# for i in range(1, n + 1, 2):
#     s += i
# print(s)

# cách 2: Dùng công thức
n = int(input())
print((n // 2 + 1) ** 2)