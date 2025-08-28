'''
Xây dựng chương trình có sử dụng khuôn hình, áp dụng cho bài sau:

Viết chương trình nhập vào 1 dãy số gồm nhiều loại số, yêu cầu xuất ra tổng của từng loại số ra màn hình.

Với các qui ước:

o   Kiểu a: là số nguyên

o   Kiểu b: là số phân số

Dữ liệu đầu vào:

o   Gồm nhiều dòng còn lại, mỗi dòng chứa kiểu và 1 số thuộc kiểu đó

Dữ liệu đầu ra: Ghi ra 2 dòng:

o   Dòng 1: tổng của loại số nguyên

o   Dòng 2: tổng của loại phân số (kết quả đã được rút gọn)

Nếu không tìm thấy tổng của loại nào thì xuất kết quả “khong co” (chữ thường, không dấu) tại vị trí của loại đó

         

Ví dụ 1:

Input:

a 1

b  1 2

b  2 3

Output:
1
7/6

 
Ví dụ 1:

Input:

b  1 2

b  2 3

 

Output:
khong co
7/6

'''
import sys
from fractions import Fraction

def main():
    sum_int = None
    sum_frac = None
    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue
        parts = s.split()
        t = parts[0]
        if t == 'a' and len(parts) >= 2:
            try:
                v = int(parts[1])
            except:
                continue
            if sum_int is None:
                sum_int = v
            else:
                sum_int += v
        elif t == 'b' and len(parts) >= 3:
            try:
                n = int(parts[1])
                d = int(parts[2])
                if d == 0:
                    continue
                f = Fraction(n, d)
            except:
                continue
            if sum_frac is None:
                sum_frac = f
            else:
                sum_frac += f
    if sum_int is None:
        print("khong co")
    else:
        print(sum_int)
    if sum_frac is None:
        print("khong co")
    else:
        num, den = sum_frac.numerator, sum_frac.denominator
        print(f"{num}/{den}")

if __name__ == "__main__":
    main()