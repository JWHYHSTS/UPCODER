'''
Xây dựng chương trình có sử dụng khuôn hình, áp dụng cho bài sau:

Viết chương trình nhập vào 1 dãy số gồm nhiều loại số, yêu cầu xuất ra tổng của từng loại số ra màn hình.

Với các qui ước:

o   Kiểu T: là số nguyên

o   Kiểu D: là SoDao (đã được mô tả ở đây)

Dữ liệu đầu vào:

o   Gồm nhiều dòng còn lại, mỗi dòng chứa kiểu và 1 số thuộc kiểu đó

Dữ liệu đầu ra:

Ghi ra 3 dòng:

·         Dòng 1: tổng của loại số nguyên

·         Dong 2: số lớn nhất của loại số nguyên

·         Dòng 3: tổng của loại SoDao

·         Dòng 4: số lớn nhất của loại SoDao

Nếu không tìm thấy tổng, số lớn nhất của loại nào thì xuất kết quả “khong co” (chữ thường, không dấu) tại vị trí của loại đó

Ví dụ 1:

Input:

T 1

D 127

T 3

D  456

Output:
4
3
1375
[SoDao] 127

Ví dụ 2:

Input:

D 127

D  456

 
Output:
khong co
khong co
1375
[SoDao] 127
              
'''

import sys

sum_int = 0
have_int = False
max_int = None

sum_sd = 0
have_sd = False
max_sd_val = None
max_sd_orig = None

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    if len(parts) < 2:
        continue
    t, num_str = parts[0], parts[1]
    try:
        n = int(num_str)
    except:
        continue
    if t == 'T':
        sum_int += n
        have_int = True
        if max_int is None or n > max_int:
            max_int = n
    elif t == 'D':
        rev = int(str(abs(n))[::-1])
        sum_sd += rev
        have_sd = True
        if max_sd_val is None or rev > max_sd_val:
            max_sd_val = rev
            max_sd_orig = n

if have_int:
    print(sum_int)
else:
    print("khong co")
if have_int:
    print(max_int)
else:
    print("khong co")
if have_sd:
    print(sum_sd)
else:
    print("khong co")
if have_sd:
    print(f"[SoDao] {max_sd_orig}")
else:
    print("khong co")