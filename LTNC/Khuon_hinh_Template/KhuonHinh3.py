'''
Xây dựng 1 cấu trúc mảng có sử dụng khuôn hình, áp dụng cho bài sau:

Viết chương trình nhập vào 1 dãy số, yêu cầu xuất ra số nhỏ nhất của từng loại số ra màn hình.

Với các qui ước:

o   Kiểu a: là số nguyên

o   Kiểu b: là số thực

o   Kiểu c: là phân số

Dữ liệu đầu vào:

o   Gồm nhiều dòng còn lại, mỗi dòng chứa kiểu và 1 số thuộc kiểu đó

Dữ liệu đầu ra:

Ghi ra 3 dòng:

o   Dòng 1: số nhỏ nhất của loại số nguyên

o   Dòng 2: số nhỏ nhất của loại số thực.

o   Dòng 3: số nhỏ nhất của loại phân số.

Nếu không tìm thấy số nhỏ nhất của loại nào thì xuất kết quả “khong co” (chữ thường, không dấu) tại vị trí của loại đó

    

Ví dụ 1:

Input:

a 1

b 1.2

c  1 2

b  2.4

c  2 3

Output:
1
1.2
1/2

 

Ví dụ 2:

Input:

b 1.2

c  1 2

b  2.4

c  2 3

 

Output:
khong co
1.2
1/2
         
'''

import sys
from decimal import Decimal, getcontext, InvalidOperation
from fractions import Fraction

getcontext().prec = 50

def fmt_decimal(d: Decimal) -> str:
    try:
        nd = d.normalize()
        s = format(nd, 'f')
    except (InvalidOperation, ValueError):
        s = str(d)
    return s

def main():
    min_int = None
    min_float = None
    min_frac = None
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
            if min_int is None or v < min_int:
                min_int = v
        elif t == 'b' and len(parts) >= 2:
            try:
                d = Decimal(parts[1])
            except:
                continue
            if min_float is None or d < min_float:
                min_float = d
        elif t == 'c' and len(parts) >= 3:
            try:
                n = int(parts[1])
                den = int(parts[2])
                if den == 0:
                    continue
                f = Fraction(n, den)
            except:
                continue
            if min_frac is None or f < min_frac:
                min_frac = f
    if min_int is None:
        print("khong co")
    else:
        print(min_int)
    if min_float is None:
        print("khong co")
    else:
        print(fmt_decimal(min_float))
    if min_frac is None:
        print("khong co")
    else:
        num, den = min_frac.numerator, min_frac.denominator
        print(f"{num}/{den}")

if __name__ == "__main__":
    main()