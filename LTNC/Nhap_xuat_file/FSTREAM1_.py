'''
SỐ CHÍNH PHƯƠNG

Nhập vào 1 số và kiểm tra số đó có phải là số chính phương không?

dữ liệu vào từ file "FSTREAM.inp":
dòng 1 : số nguyên n

dữ liệu xuất ra file "FSTREAM.out":
dòng 1 : Xuất: "YES" nếu đó là số chính phương, ngược lại xuất "NO"

input: 4
output: YES
'''
import math

with open("FSTREAM.inp", "r") as f:
    n = int(f.readline().strip())

sqrt_n = int(math.sqrt(n))
result = "YES" if sqrt_n * sqrt_n == n else "NO"

with open("FSTREAM.out", "w") as f:
    f.write(result)