'''
Cho hai số nguyên dương a và b (a < b, a và b không vượt quá 1000). Hãy liệt kê tất cả các số nguyên trong đoạn [a, b] nếu tổng các chữ số của số nguyên đó là số nguyên tố. 
Ví dụ:

Input
10 15
Output
11 12 14 
Giải thích: Trong đoạn từ 10 đến 15 ta có
10 => 1 + 0 = 1 => 1 không phải số nguyên tố.
11 => 1 + 1 = 2 => 2 là số nguyên tố.
12 => 1 + 2 = 3 => 3 là số nguyên tố.
13 => 1 + 3 = 4 => 4 không phải số nguyên tố.
14 => 1 + 4 = 5 => 5 là số nguyên tố.
15 => 1 + 5 = 6 => 6 không phải số nguyên tố.

'''
a, b = map(int, input().strip().split())
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
for i in range(a, b + 1):
    digit_sum = sum(int(d) for d in str(i))
    if snt(digit_sum):
        print(i, end=' ')