'''
Xây dựng 1 cấu trúc mảng (hoặc lớp) có sử dụng khuôn hình, áp dụng cho bài sau:

          Viết chương trình nhập vào 1 dãy số, yêu cầu xuất ra tổng của các dãy số đó ra màn hình.

Với các qui ước:

-      Kiểu a: là số nguyên

-      Kiểu b: là phân số

Dữ liệu đầu vào:

-      Dòng đầu tiên: nhập vào loại kiểu của dãy số (kiểu a hoặc b)

-      Các dòng còn lại, mỗi dòng chứa 1 số thuộc kiểu của dòng đầu tiên

Dữ liệu đầu ra:

-      Gồm 1 số duy nhất (thuộc kiểu đã cho).

Lưu ý:  

- Nếu kết quả là phân số thì phân số đó đã được rút gọn.

    

Ví dụ 1:

Input:

a

1

2

3

4

Output:
10

Ví dụ 2:

Input:

b

1 2

2 3

3 4

4 5

Output:
163/60

'''

from fractions import Fraction
import sys

def main():
    lines = [ln.strip() for ln in sys.stdin.read().splitlines() if ln.strip() != ""]
    if not lines:
        return
    t = lines[0].strip().lower()
    data = lines[1:]

    if t == 'a':
        total = 0
        for line in data:
            for tok in line.split():
                if tok:
                    total += int(tok)
        print(total)

    elif t == 'b':
        total = Fraction(0, 1)
        for line in data:
            if not line:
                continue
            tokens = line.split()
            if len(tokens) == 1 and '/' in tokens[0]:
                n_str, d_str = tokens[0].split('/', 1)
                total += Fraction(int(n_str), int(d_str))
            elif len(tokens) >= 2:
                total += Fraction(int(tokens[0]), int(tokens[1]))
            else:
                total += Fraction(int(tokens[0]), 1)
        print(f"{total.numerator}/{total.denominator}")

if __name__ == "__main__":
    main()