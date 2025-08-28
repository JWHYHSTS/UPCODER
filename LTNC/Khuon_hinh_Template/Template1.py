'''
Viết 1 hàm template tìm phần tử lớn nhất trong 3 số.
Yêu cầu xuất phần tử lớn nhất trong 3 số.

qui ước: a là số nguyên, b là số thực, c là phân số
(các số nhập <= 100)

ví dụ:
a 1 2 3 tức là nhập 3 số nguyên

Dữ liệu vào:
Dòng 1: là nhập vào loại số
3 dòng tiếp theo: mỗi dòng chứa 1 số thuộc kiểu của dòng 1

Dữ liệu ra: gồm 1 dòng là số lớn nhất tìm thấy
Ví dụ 1:

Input
a
1
2
3
Output
3

Ví dụ 2:
Input
c
1 2
1 1
2 3
Output
1/1

'''
from fractions import Fraction
import sys
import math

def read_input():
    data = sys.stdin.read().strip().splitlines()
    return [line.strip() for line in data if line.strip() != ""]

def format_float(x: float) -> str:
    if math.isclose(x, int(round(x))):
        return str(int(round(x)))
    # Remove trailing zeros while keeping necessary precision
    s = f"{x:.12g}"
    return s

def main():
    lines = read_input()
    if not lines:
        return
    t = lines[0]
    vals = lines[1:]
    if len(vals) != 3:
        return  # or handle error
    if t == 'a':
        nums = [int(v) for v in vals]
        print(max(nums))
    elif t == 'b':
        nums = [float(v) for v in vals]
        m = max(nums)
        print(format_float(m))
    elif t == 'c':
        fracs = []
        for line in vals:
            parts = line.split()
            if len(parts) != 2:
                return
            num, den = map(int, parts)
            f = Fraction(num, den)
            fracs.append(f)
        m = max(fracs)
        # Output as numerator/denominator (already reduced)
        print(f"{m.numerator}/{m.denominator}")
    else:
        return

if __name__ == "__main__":
    main()