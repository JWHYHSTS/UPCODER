'''
Như ta đã biết, một số nguyên dương được gọi là số nguyên tố khi nó chỉ có đúng 2 ước là 1 và chính nó.

Theo định nghĩa đó, các số nguyên tố đầu tiên là: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41 ...

Yêu cầu:

Cho một đoạn [A; B]. Bạn hãy tính tổng tất cả các số nguyên tố X nằm trong đoạn [A; B] sao cho X mod m = n.

Input:

Số nguyên dương T - số lượng test (T <= 100)
T dòng tiếp theo, mỗi dòng gồm 4 số A, B, m, n
(1 <= A, B <= 100.000, 0 <= n < m <= B)

Output:

T dòng, mỗi dòng là kết quả của bộ test tương ứng.

Ví dụ:

Input	Output
2
10 30 3 2
1 10 4 1
80
5

Giải thích ví dụ mẫu:

Test 1: Các số nguyên tố trong đoạn [10; 30] là: 11, 13, 17, 19, 23, 29.
Ta cần tính tổng các số chia cho 3 dư 2. Vậy tổng cần tính là: 11 + 17 + 23 + 29 = 80
Test 2: Các số nguyên tố trong đoạn [1; 10] là: 2, 3, 5, 7.
Ta cần tính tổng các số chia cho 4 dư 1. Vậy đáp án là: 5

'''
import sys

data = list(map(int, sys.stdin.read().strip().split()))
if not data:
    sys.exit(0)

t = data[0]
tests = []
idx = 1
maxB = 0
for _ in range(t):
    if idx + 3 >= len(data):
        break
    A, B, m, n = data[idx:idx+4]
    idx += 4
    if B > maxB:
        maxB = B
    tests.append((A, B, m, n))

limit = maxB
is_prime = [True]*(limit+1)
if limit >= 0:
    is_prime[:2] = [False, False] if limit >= 1 else [False]
p = 2
while p*p <= limit:
    if is_prime[p]:
        step = p
        start = p*p
        is_prime[start:limit+1:step] = [False]*(((limit - start)//step)+1)
    p += 1

primes = [i for i in range(2, limit+1) if is_prime[i]]

out_lines = []
for A, B, m, n in tests:
    if A > B:
        A, B = B, A
    s = 0

    import bisect
    l = bisect.bisect_left(primes, A)
    r = bisect.bisect_right(primes, B)
    for p in primes[l:r]:
        if p % m == n:
            s += p
    out_lines.append(str(s))

sys.stdout.write("\n".join(out_lines))