'''
Input:
Nhập vào 1 số gồm 4 chữ số
Output:
Tính tổng chữ số nhỏ nhất và chữ số lớn nhất của số trong input
Ví dụ:

Input	
1234
Output
5
'''
import sys
data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)
s = data[0]
digits = [int(ch) for ch in s if ch.isdigit()][:4]
if len(digits) != 4:
    sys.exit(0)
tong = min(digits) + max(digits)
print(tong, end="")