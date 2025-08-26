'''
Cho cấu trúc lưu trữ Phân số, bao gồm 2 số nguyên cho biết tử số và mẫu số
Viết chương trình nhập vào một mảng Phân số và xuất ra mảng các Phân số được sắp xếp tăng dần theo gía trị.
Yêu cầu:
- Sử dụng kĩ thuật nạp chồng toán tử so sánh lớn, bé để so sánh 2 phân số, phục vụ cho thuật toán sắp xếp.

Dữ liệu đầu vào:
- Dòng đầu tiên chứa số nguyên N (0 < N <= 20)
- N dòng tiếp theo, mỗi dòng chứa một Phân số, bao gồm 2 số nguyên cho biết tử số và mẫu số. Mỗi số nguyên cách nhau bởi 1 khoảng trắng.
Dữ liệu đầu ra:
- Dãy phân số được sắp xếp tăng dần theo giá trị. Mỗi phân số bao gồm tử và mẫu đã được tối giản và được xuất theo định dạng tử/mẫu. Mỗi phân số cách nhau bởi 1 khoảng trắng.

Vd:
input:
5
4 2
6 8
18 15
7 8
2 6
output:
1/3 3/4 7/8 6/5 2/1

'''
from dataclasses import dataclass
from math import gcd
import sys

@dataclass
class Fraction:
    tu: int
    mau: int

    def __post_init__(self):
        if self.mau == 0:
            raise ValueError("Mau so khong duoc bang 0")
        if self.mau < 0:
            self.tu = -self.tu
            self.mau = -self.mau
        if self.tu == 0:
            self.mau = 1
        else:
            g = gcd(abs(self.tu), self.mau)
            self.tu //= g
            self.mau //= g

    def __lt__(self, other):
        return self.tu * other.mau < other.tu * self.mau

    def __gt__(self, other):
        return self.tu * other.mau > other.tu * self.mau

    def __str__(self):
        return f"{self.tu}/{self.mau}"

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    fracs = []
    idx = 1
    for _ in range(n):
        tu = int(data[idx]); mau = int(data[idx+1]); idx += 2
        fracs.append(Fraction(tu, mau))
    fracs.sort()
    print(" ".join(str(f) for f in fracs))

if __name__ == "__main__":
    main()