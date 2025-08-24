'''
Nhập vào một số nguyên, xác định xem số đó có phải là số nguyên tố hay không? Kết quả trả về là 1 (nếu là số nguyên tố) hoặc 0 (nếu không phải là số nguyên tố). VD input 10 - output 0, input 2 - output 1
'''
import sys, math

def snt(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

n = int(data[0])
print(1 if snt(n) else 0, end="")

