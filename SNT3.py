'''
Hãy tìm tất cả các số nguyên tố trong đoạn [A,B] .

Input:

Gồm 2 số nguyên A và B cách nhau bởi 1 dấu cách ( 1 ≤ A ≤ B ≤ 200000 ) .

Output:

Ghi ra tất cả các số nguyên tố trong đoạn [A,B]. Mỗi số trên 1 dòng .

Ví dụ

Input:

1 10

Output:

2

3

5

7

'''
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

A, B = map(int, input().split())
for num in range(A, B + 1):
    if is_prime(num):
        print(num)