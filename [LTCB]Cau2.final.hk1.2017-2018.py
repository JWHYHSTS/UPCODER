'''
Cho một dãy nhị phân với độ dài tối đa là N bits (N là số nguyên dương không quá 10000). Hãy viết chương trình nhập vào dãy nhị phân đó và thực hiện các yêu cầu sau:

1.      Đếm số lượng bit 0 và 1 có trong dãy

2.      Cho biết dãy bit 1 liên tiếp dài nhất trong dãy nhị phân có độ dài là bao nhiêu?

* Gợi ý: dùng mảng kí tự để lưu dãy nhị phân.

Ví dụ:

Cho dãy nhị phân 01001101110101111

Số lượng bit 0 là 6; số lượng bit 1 là 11

Dãy bit 1 liên tiếp dài nhất có độ dài là 4

Input:

-          Dòng thứ nhất: số nguyên N cho biết độ dài dãy nhị phân

-          Dòng thứ hai: N kí tự (0 hoặc 1) liên tiếp nhau

Output:

-          Dòng thứ nhất: 2 số nguyên cho biết số lượng bit 0 và số lượng bit 1 có trong dãy.

-          Dòng thứ hai: số nguyên cho biết độ dài của dãy bit 1 liên tiếp dài nhất trong dãy.



Ví dụ:


Input	
17
01001101110101111
Output
6 11
4
'''

import sys

line = sys.stdin.readline()
if not line:
    sys.exit(0)
N = int(line.strip())

bits = ""
while len(bits) < N:
    line = sys.stdin.readline()
    if not line:
        break
    for ch in line.strip():
        if ch in '01':
            bits += ch
            if len(bits) == N:
                break

bits = bits[:N]

cnt0 = bits.count('0')
cnt1 = N - cnt0

max_run = cur = 0
for ch in bits:
    if ch == '1':
        cur += 1
        if cur > max_run:
            max_run = cur
    else:
        cur = 0

print(cnt0, cnt1)
print(max_run)