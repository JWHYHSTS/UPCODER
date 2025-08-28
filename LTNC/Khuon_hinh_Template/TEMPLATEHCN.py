'''
Xây dựng 1 cấu trúc mảng có sử dụng khuôn hình, áp dụng cho bài sau:

Viết chương trình nhập vào 1 dãy số, yêu cầu xuất ra số nhỏ nhất và tổng của các dãy số đó ra màn hình.

Với các qui ước:

-  Kiểu N: là số nguyên ( <=1000)

-  Kiểu H: là hình chữ nhật (được mô tả ở đây)

Dữ liệu đầu vào:

- Dòng đầu tiên: nhập vào loại kiểu của dãy số (kiểu a hoặc b)

- Các dòng còn lại, mỗi dòng chứa 1 số thuộc kiểu của dòng đầu tiên

Dữ liệu đầu ra:

-          Dòng 1: số nhỏ nhất (thuộc kiểu đã cho).

-          Dòng 2: tổng của dãy số.

Lưu ý:  

-          Nếu kết quả là hình chữ nhật thì tổng dãy chỉ lấy chính xác 1 chữ số thập phân.

-          Số lượng phần tử của dãy <= 100

 

Ví dụ 1:

Input:

N

1

2

3

4

Output:
1
10

Ví dụ 2:

Input:

H

1 2

2 3

3 4

4 5

Output:
[HCN] 1,2
48.0
'''

import sys
data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)
t = data[0]
tokens = data[1:]
if t == 'N':
    vals = [int(x) for x in tokens] if tokens else []
    if not vals:
        sys.exit(0)
    print(min(vals))
    print(sum(vals))
elif t == 'H':
    pairs = []
    i = 0
    n = len(tokens)
    while i+1 < n:
        w = int(tokens[i]); h = int(tokens[i+1])
        pairs.append((w,h))
        i += 2
    if not pairs:
        sys.exit(0)
    def area_key(p):
        return (p[0]*p[1], p[0], p[1])
    mn = min(pairs, key=area_key)
    total_perimeter = sum(2*(w+h) for w,h in pairs)
    print(f"[HCN] {mn[0]},{mn[1]}")
    print(f"{total_perimeter:.1f}")
else:
    sys.exit(0)