'''
Số nguyên tố là số tự nhiên lớn hơn 1 không phải là tích của hai số tự nhiên nhỏ hơn. Nói cách khác, số nguyên tố là những số chỉ có đúng hai ước số là 1 và chính nó.

Nhập vào 1 số nguyên n, yêu cầu xuất tất cả số nguyên tố từ 1 đến n (mỗi số cách 1 khoảng trắng) - nếu không có số nào, xuất -1

ví dụ:

input:
5

output
2 3 5


'''

n = int(input().strip())
if n < 2:
    print(-1)
else:
    def is_prime(x: int) -> bool:
        if x < 2: return False
        if x == 2: return True
        if x % 2 == 0: return False
        r = int(x ** 0.5)
        for i in range(3, r + 1, 2):
            if x % i == 0:
                return False
        return True
    primes = [str(i) for i in range(2, n + 1) if is_prime(i)]
    print(" ".join(primes) if primes else "-1") 