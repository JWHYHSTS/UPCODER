'''
Input: 
1 số nguyên n
ouput: 
kết quả của phép toán: 1+1/23+1/33+...+1/n3 
(kết quả lấy 3 chữ số thập phân)

ví dụ:
input:
3

output:
1.162

'''
import sys, math

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)
n = int(data[0])

s = math.fsum(1.0 / (i**3) for i in range(1, n + 1))

print(f"{s:.3f}", end="")