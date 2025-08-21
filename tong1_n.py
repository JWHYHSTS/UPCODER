'''
Nhập vào số n.

Xuất tổng từ 1 đến n
'''
n = int(input())
print(n * (n + 1) // 2)

# Cách 2: Dùng for
'''
n = int(input())
s = 0
for i in range(1, n + 1):
    s += i
print(s)
'''