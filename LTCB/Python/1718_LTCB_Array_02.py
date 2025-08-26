'''
Cho 1 mảng các số nguyên. Hãy tách các số là số nguyên tố, số hoàn chỉnh, số chính phương thành từng mảng riêng.

Gợi ý: 
- Số nguyên tố là số chỉ có 2 ước số là 1 và chính nó. Vd: 2, 3, 5, 7, 11, 13, ...
- Số chính phương là số có giá trị bằng bình phương của 1 số nguyên. Vd: 1, 4, 9, 16, 25, 36, ...
- Số hoàn chỉnh là số có tổng các ước số (ngoại trừ chính nó) bằng chính nó. Vd: 6 (1+2+3), 28 (1+2+4+7+14), ...
- Sử dụng 3 mảng ứng với từng loại số.
- Với mỗi số nguyên nhập vào, kiểm tra đó là loại số gì để thêm vào từng mảng tương ứng. Lưu ý thứ tự của các số khi thêm vào mảng.

Input:
- Dòng 1: số nguyên N
- Dòng 2: N số nguyên, mỗi số cách nhau 1 khoảng trắng.
Output:
- Dòng 1: in mảng các số nguyên tố
- Dòng 2: in mảng các số chính phương
- Dòng 3: in mảng các số hoàn chỉnh
*Lưu ý: nếu mảng rỗng thì in ra chữ "NULL"

Ví dụ:

Input	Output
6
1 2 3 4 5 6
2 3 5
1 4
6

Lưu ý: Xuất "chính xác" từng khoảng trắng. Không dư khoảng trắng cuối dòng hoăc dư dòng trống.

'''
import math
import sys

def is_prime(x: int) -> bool:
    if x <= 1: return False
    if x <= 3: return True
    if x % 2 == 0 or x % 3 == 0: return False
    r = int(math.isqrt(x))
    i = 5
    while i <= r:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

def is_square(x: int) -> bool:
    if x < 0: return False
    r = math.isqrt(x)
    return r * r == x

def is_perfect(x: int) -> bool:
    if x < 2: return False
    s = 1
    r = int(math.isqrt(x))
    for d in range(2, r + 1):
        if x % d == 0:
            s += d
            q = x // d
            if q != d:
                s += q
        if s > x:  # cắt sớm
            return False
    return s == x


data_iter = iter(sys.stdin.read().strip().split())
try:
    n = int(next(data_iter))
except StopIteration:
    sys.exit(0)

nums = []
for _ in range(n):
    try:
        nums.append(int(next(data_iter)))
    except StopIteration:
        break 
primes = []
squares = []
perfects = []

for v in nums:
    if is_prime(v):
        primes.append(v)
    elif is_square(v):        
        squares.append(v)
    elif is_perfect(v):      
        perfects.append(v)

def out(arr, last=False):
    if arr:
        line = " ".join(map(str, arr))
    else:
        line = "NULL"

    if last:
        print(line, end="")
    else:
        print(line)

out(primes)
out(squares)
out(perfects, last=True)