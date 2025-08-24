'''
Nhập vào 1 số nguyên n, yêu cầu xuất tất cả số nguyên tố từ 1 đến n (mỗi số cách 1 khoảng trắng) - nếu không có số nào, xuất -1


Ví dụ:

input:
5

output
2 3 5
'''

def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input().strip())
primes = [i for i in range(1, n + 1) if snt(i)]
print(" ".join(map(str, primes)) if primes else "-1")