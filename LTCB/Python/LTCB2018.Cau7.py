'''
SỐ KỲ DIỆU

Số nguyên dương X được gọi là số kỳ diệu nếu nó bằng hiệu của số lớn nhất (được tạo thành từ các chữ số của nó) với số nhỏ nhất (được tạo thành từ các chữ số của nó).

Yêu cầu: Cho số nguyên dương X, hãy xác định xem X có phải số kỳ diệu hay không.
Input:
Số nguyên dương X (0 < X < 10^9)
Output:
Dòng 1: Nếu X là số kỳ diệu thì xuất "YES", ngược lại xuất "NO" (không xuất dấu ngoặc kép).
Dòng 2: Xuất 2 số nguyên dương A, B cách nhau một khoảng trắng. Trong đó A là số lớn nhất và B là số nhỏ nhất được tạo thành từ các chữ số của X.
Ví dụ 1:
Input	
495
Output
YES
954 459
Giải thích:
495 là số kỳ diệu, vì số lớn nhất và số nhỏ nhất được tạo thành từ các chữ số của nó lần lượt là: 495 và 459. Hiệu 2 số này bằng 495.

Ví dụ 2:
Input	
123
Output
NO
321 123
Giải thích:
123 không phải số kỳ diệu, vì số lớn nhất và số nhỏ nhất được tạo thành từ các chữ số của nó lần lượt là: 321 và 123. Hiệu 2 số này khác 123.
'''

import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)
x_str = data[0]
X = int(x_str)

digits = list(x_str)
A_str = ''.join(sorted(digits, reverse=True))
A = int(A_str)

asc = sorted(digits)
if asc[0] == '0':
    for i in range(1, len(asc)):
        if asc[i] != '0':
            asc[0], asc[i] = asc[i], asc[0]
            break
B_str = ''.join(asc)
B = int(B_str)

print("YES" if A - B == X else "NO")
print(f"{A} {B}")