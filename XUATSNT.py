'''
Nhập vào 1 số nguyên n, yêu cầu xuất tất cả số nguyên tố từ 1 đến n (mỗi số cách 1 khoảng trắng) - nếu không có số nào, xuất -1


ví dụ:

input:
5

output
2 3 5
'''
n = int(input())
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

found = False
for i in range(2, n + 1):
    if is_prime(i):
        print(i, end=" ")
        found = True
if not found:
    print(-1)